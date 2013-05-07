from PyQt4 import QtGui
from Ui_AboutDialog import Ui_AboutDialog

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.ui.applicationAuthor.setText("Vladimir Kolev")
        self.ui.applicationComment.setText("qExFmPlayer is a desktop application for listening music from the ex.fm Service")
        self.ui.applicationName.setText("qExFmPlayer 0.1a")
        # use new style signals
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    def accept(self):
        super(MyDialog, self).accept()