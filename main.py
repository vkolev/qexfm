#!/usr/bin/env python2

import os
import sys
from exfm.ExFmlib import ExFmLib
from exfm.SongWidgetItem import SongWidgetItem
from exfm.TruncatedLabel import TruncatedLabel
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from AboutDialog import MyDialog

PATH = os.path.realpath(__file__).replace('main.py', '')


GANRES = ["Blues", "Chillwave", "Classical", "Country",
"Dubstep", "Electronica", "Experimental", "Folk", "Hip-hop",
"House", "Indie", "Jazz", "Mashup", "Metal", "Pop", "Punk",
"Reggae", "Rock", "Shoegaze", "Soul", "Synthpop"]


class ExfmPlayer(QtGui.QMainWindow):

    def __init__(self):
        super(ExfmPlayer, self).__init__()
        self.songs = []
        self.currentPosition = None
        self.currentSong = None
        self.searchTerm = ""
        self.m_media = None
        self.lastsearch = ""
        self.initUI()

    def initUI(self):
        # SearchBox
        self.searchBox = QtGui.QLineEdit(self)
        self.searchBox.setPlaceholderText("Search...")
        self.searchBox.setMaximumWidth(200)
        self.searchBox.clearFocus()
        self.searchBox.returnPressed.connect(self.do_search)
        self.searchBoxWidget = QtGui.QWidgetAction(self)
        self.searchBoxWidget.setDefaultWidget(self.searchBox)

        # prevButton
        prevAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/prev24.svg')), 'Previous', self)
        prevAction.setShortcut('Ctrl+B')
        prevAction.triggered.connect(self.previous_song)

        # playButton
        self.playAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/play24.svg')), 'Play/Stop', self)
        self.playAction.setShortcut('Ctrl+P')
        self.playAction.triggered.connect(self.play_song)

        # nextButton
        nextAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/next24.svg')), 'Next', self)
        nextAction.setShortcut('Ctrl+N')
        nextAction.triggered.connect(self.next_song)

        # saveButton
        saveAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/save24.svg')), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save_song)

        # CurrentSong
        self.currentSongLabel = TruncatedLabel()
        font = QtGui.QFont()
        font.setPointSize(9)
        titleSeek = QtGui.QVBoxLayout()
        titleSeek.setSpacing(0)
        playContainer = QtGui.QWidget()
        self.currentSongLabel.setText("Artist - Title")
        self.currentSongLabel.setFont(font)
        self.currentSongLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentSongLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.seeker = Phonon.SeekSlider()
        self.seeker.setIconVisible(False)
        titleSeek.addWidget(self.currentSongLabel)
        titleSeek.addWidget(self.seeker)
        playContainer.setLayout(titleSeek)
        spacerActionWidget = QtGui.QWidgetAction(self)
        spacerActionWidget.setDefaultWidget(playContainer)

        # The ToolButton
        self.toolButton = QtGui.QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon(os.path.join(PATH, 'data/cogs24.svg')))
        self.toolButton.setPopupMode(2)
        self.toolButton.setArrowType(0)
        self.toolButton.setMenu(self.__menu())
        toolButtonWidget = QtGui.QWidgetAction(self)
        toolButtonWidget.setDefaultWidget(self.toolButton)

        self.toolbar = self.addToolBar('Main')
        self.toolbar.setMovable(False)
        self.toolbar.addAction(self.searchBoxWidget)
        self.toolbar.addSeparator()
        self.toolbar.addAction(prevAction)
        self.toolbar.addAction(self.playAction)
        self.toolbar.addAction(nextAction)
        self.toolbar.addSeparator()
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(spacerActionWidget)
        self.toolbar.addAction(toolButtonWidget)
        
        vbox = QtGui.QVBoxLayout()
        container = QtGui.QWidget()
        self.comboBox = QtGui.QComboBox()
        self.comboBox.addItem(QtGui.QIcon(os.path.join(PATH, 'data/trending_icon.png')), 'Trending')
        self.comboBox.addItem(QtGui.QIcon(os.path.join(PATH, 'data/explore_icon.png')), 'Explore')
        self.comboBox.addItem(QtGui.QIcon(os.path.join(PATH, 'data/sites_icon.png')), 'Sites')
        self.comboBox.currentIndexChanged.connect(self.site_changed);
        container.setMaximumWidth(200)
        self.leftlist = QtGui.QListWidget(self)
        self.leftlist.setFrameShape(QtGui.QFrame.NoFrame)
        self.leftlist.setMaximumWidth(200)
        self.leftlist.addItems(GANRES)
        self.leftlist.itemDoubleClicked.connect(self.change_music)
        vbox.addWidget(self.comboBox)
        vbox.addWidget(self.leftlist)
        container.setLayout(vbox)
        self.rightlist = QtGui.QListWidget(self)
        self.scrollbarRight = self.rightlist.verticalScrollBar()
        self.scrollbarRight.sliderReleased.connect(self.load_more)
        self.rightlist.itemDoubleClicked.connect(self.play_song)
        
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(container)
        splitter.addWidget(self.rightlist)
        
        self.setCentralWidget(splitter)
        self.setMinimumSize(800, 500)
        self.setWindowTitle('ExfmPlayer')
        self.setWindowIcon(QtGui.QIcon(os.path.join(PATH, 'data/exfmplayer24.png')))
        self.show()

    def __menu(self):
        menu = QtGui.QMenu()
        aboutAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/about24.svg')), 'About', self)
        aboutAction.triggered.connect(self.show_about)
        exitAction = QtGui.QAction(QtGui.QIcon(os.path.join(PATH, 'data/exit24.svg')), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        menu.addAction(aboutAction)
        menu.addAction(exitAction)
        return menu

    def show_about(self, sender):
        aboutDlg = MyDialog(self)
        aboutDlg.exec_()
        

    def previous_song(self, sender):
        if self.currentPosition == None:
            self.currentPosition = self.rightlist.count() - 1
        else:
            self.currentPosition -= 1
        songWidget = self.rightlist.item(self.currentPosition)
        songWidget.setSelected(True)
        self.currentSong = songWidget.get_song()
        self.currentSongLabel.setText("%s - %s" % (self.currentSong.artist, self.currentSong.title))
        output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, output)
        self.m_media.setCurrentSource(Phonon.MediaSource(QtCore.QUrl(self.currentSong.get_url())))
        self.seeker.setMediaObject(self.m_media)
        self.m_media.finished.connect(self.next_song)
        self.playAction.setIcon(QtGui.QIcon(os.path.join(PATH, 'data/pause24.svg')))
        self.m_media.play()

    def play_song(self, sender):
        if self.currentSong is None:
            if type(sender) is bool:
                pass
            elif type(sender) is QtGui.QListWidgetItem:
                self.do_search()
            else:
                self.playAction.setIcon(QtGui.QIcon(os.path.join(PATH, 'data/pause24.svg')))
                self.currentSong = sender.get_song()
                self.currentPosition = self.rightlist.currentRow()
                self.currentSongLabel.setText("%s - %s" % (self.currentSong.artist, self.currentSong.title))
                self.start_player()
        else:
            if type(sender) is not SongWidgetItem:
                self.currentSong = None
                self.playAction.setIcon(QtGui.QIcon(os.path.join(PATH, 'data/play24.svg')))
                self.currentSongLabel.setText("Artist - Title")
                self.m_media.stop()
            elif type(sender) is QtGui.QListWidgetItem:
                self.do_search()
            else:
                self.currentSong = sender.get_song()
                self.currentSongLabel.setText("%s - %s" % (self.currentSong.artist, self.currentSong.title))
                self.currentPosition = sender.index()
                self.currentPosition = 0
                self.start_player()
        print "Play/Stop Button pressed"
        
    def start_player(self):
        output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, output)
        self.m_media.setCurrentSource(Phonon.MediaSource(QtCore.QUrl(self.currentSong.get_url())))
        self.seeker.setMediaObject(self.m_media)
        self.m_media.finished.connect(self.next_song)
        self.m_media.play()
        

    def next_song(self):
        if self.currentPosition == None:
            self.currentPosition = 0
        else:
            self.currentPosition += 1
        songWidget = self.rightlist.item(self.currentPosition)
        songWidget.setSelected(True)
        self.currentSong = songWidget.get_song()
        self.currentSongLabel.setText("%s - %s" % (self.currentSong.artist, self.currentSong.title))
        output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.m_media = Phonon.MediaObject()
        Phonon.createPath(self.m_media, output)
        self.m_media.setCurrentSource(Phonon.MediaSource(QtCore.QUrl(self.currentSong.get_url())))
        self.seeker.setMediaObject(self.m_media)
        self.m_media.finished.connect(self.next_song)
        self.playAction.setIcon(QtGui.QIcon(os.path.join(PATH, 'data/pause24.svg')))
        self.m_media.play()
        
    def load_more(self, sender=None):
        client = ExFmLib()
        print "Maximum %i" % self.scrollbarRight.maximum()
        if self.rightlist.count() < 100:
            search = client.get_search(self.searchTerm, self.rightlist.count(), 20)
            for song in search.songs:
                try:
                    self.rightlist.addItem(SongWidgetItem(song, QtGui.QIcon('data/folder-music.svg')))
                except TypeError:
                    pass
            

    def do_search(self, sender=None):
        client = ExFmLib()
        term = str(self.searchBox.text())
        if self.searchTerm != term:
            self.searchTerm = term
            self.rightlist.clear()
        self.setWindowTitle("ExFmPlayer [%s]" % self.searchTerm)
        search = client.get_search(self.searchTerm, self.rightlist.count(), 20)
        for song in search.songs:
            try:
                self.rightlist.addItem(SongWidgetItem(song, QtGui.QIcon('data/folder-music.svg')))
            except TypeError:
                pass

    def save_song(self, sender):
        print "Saving current song"
        
    def change_music(self, sender):
        client = ExFmLib()
        tag = str(sender.text())
        category = str(self.comboBox.currentText())
        self.setWindowTitle("ExFmPlayer [%s in %s]" % (tag, category))
        search = None
        if category == "Trending":
            search = client.get_trending(tag.lower(), self.rightlist.count(), 20)
        elif category == "Explore":
            search = client.get_explore(tag.lower(), self.rightlist.count(), 20)
        else:
            search = client.get_trending(tag.lower(), self.rightlist.count(), 20)
        self.rightlist.clear()
        for song in search.songs:
            try:
                self.rightlist.addItem(SongWidgetItem(song,
                                QtGui.QIcon(os.path.join(PATH, 'data/folder-music.svg'))))
            except TypeError:
                pass
        
    def site_changed(self, sender):
        if sender != 2:
            self.leftlist.clear()
            self.leftlist.addItems(GANRES)
        else:
            self.leftlist.clear()
                

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('qExFmPlayer')
    player = ExfmPlayer()
    sys.exit(app.exec_())
