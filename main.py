#!/usr/bin/env python2

import sys
from exfm.ExFmlib import ExFmLib
from PyQt4 import QtGui, QtCore

GANRES = ["Blues", "Chillwave", "Classical", "Country",
"Dubstep", "Electronica", "Experimental", "Folk", "Hip-hop",
"House", "Indie", "Jazz", "Mashup", "Metal", "Pop", "Punk",
"Reggae", "Rock", "Shoegaze", "Soul", "Synthpop"]


class ExfmPlayer(QtGui.QMainWindow):

    def __init__(self):
        super(ExfmPlayer, self).__init__()
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
        prevAction = QtGui.QAction(QtGui.QIcon('data/prev24.svg'), 'Previous', self)
        prevAction.setShortcut('Ctrl+B')
        prevAction.triggered.connect(self.previous_song)

        # playButton
        self.playAction = QtGui.QAction(QtGui.QIcon('data/play24.svg'), 'Play/Stop', self)
        self.playAction.setShortcut('Ctrl+P')
        self.playAction.triggered.connect(self.play_song)

        # nextButton
        nextAction = QtGui.QAction(QtGui.QIcon('data/next24.svg'), 'Next', self)
        nextAction.setShortcut('Ctrl+N')
        nextAction.triggered.connect(self.next_song)

        # saveButton
        saveAction = QtGui.QAction(QtGui.QIcon('data/save24.svg'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.triggered.connect(self.save_song)

        # CurrentSong
        self.currentSongLabel = QtGui.QLabel()
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currentSongLabel.setText("<b>Artist</b> - Title")
        self.currentSongLabel.setFont(font)
        self.currentSongLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentSongLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        spacerActionWidget = QtGui.QWidgetAction(self)
        spacerActionWidget.setDefaultWidget(self.currentSongLabel)

        # The ToolButton
        self.toolButton = QtGui.QToolButton(self)
        self.toolButton.setIcon(QtGui.QIcon('data/cogs24.svg'))
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
        comboBox = QtGui.QComboBox()
        comboBox.addItem(QtGui.QIcon('data/trending_icon.png'), 'Trending')
        comboBox.addItem(QtGui.QIcon('data/explore_icon.png'), 'Explore')
        comboBox.addItem(QtGui.QIcon('data/sites_icon.png'), 'Sites')
        comboBox.currentIndexChanged.connect(self.site_changed);
        container.setMaximumWidth(200)
        self.leftlist = QtGui.QListWidget(self)
        self.leftlist.setMaximumWidth(200)
        self.leftlist.itemDoubleClicked.connect(self.change_music)
        vbox.addWidget(comboBox)
        vbox.addWidget(self.leftlist)
        container.setLayout(vbox)
        self.label = QtGui.QLabel('<b>Select ganre</b>')
        
        splitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter.addWidget(container)
        splitter.addWidget(self.label)
        
        self.setCentralWidget(splitter)
        self.setMinimumSize(800, 600)
        self.setWindowTitle('ExfmPlayer')
        self.setWindowIcon(QtGui.QIcon('data/exfmplayer24.png'))
        self.show()

    def __menu(self):
        menu = QtGui.QMenu()
        aboutAction = QtGui.QAction(QtGui.QIcon('data/about24.svg'), 'About', self)
        aboutAction.triggered.connect(self.show_about)
        exitAction = QtGui.QAction(QtGui.QIcon('data/exit24.svg'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(QtGui.qApp.quit)
        menu.addAction(aboutAction)
        menu.addAction(exitAction)
        return menu

    def show_about(self, sender):
        print "Show about dialog"

    def previous_song(self, sender):
        print "Prev button pressed"

    def play_song(self, sender):
        self.playAction.setIcon(QtGui.QIcon('data/pause24.svg'))
        client = ExFmLib()
        trending = client.get_trending('hip-hop', 0, 20)
        print trending.status_code
        print "Play/Stop Button pressed"

    def next_song(self, sender):
        print "Next button pressed"

    def do_search(self):
        client = ExFmLib()
        search = client.get_search(str(self.searchBox.text()), 0, 20)
        self.label.setText(search.songs[0].title)

    def save_song(self, sender):
        print "Saving current song"
        
    def change_music(self, sender):
        self.label.setText(sender.text())
        
    def site_changed(self, sender):
        if sender != 2:
            self.leftlist.clear()
            self.leftlist.addItems(GANRES)
        else:
            self.leftlist.clear()
                


def main():

    app = QtGui.QApplication(sys.argv)
    player = ExfmPlayer()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
