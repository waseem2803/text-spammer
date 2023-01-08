from PyQt5 import QtCore, QtGui, QtWidgets
import pyautogui as pt
import time

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 588)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 871, 611))
        self.widget.setStyleSheet("background-color: rgb(37, 37, 37);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(160, 140, 161, 61))
        self.label.setObjectName("label")
        self.lim = QtWidgets.QLineEdit(self.widget)
        self.lim.setGeometry(QtCore.QRect(320, 140, 261, 51))
        self.lim.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.lim.setText("")
        self.lim.setObjectName("lim")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(160, 260, 181, 81))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 270, 261, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(330, 430, 261, 61))
        self.pushButton.setStyleSheet("background-color: rgb(242, 233, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(360, 440, 191, 51))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.pushButton.clicked.connect(self.spm)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def spm(self):
        self.limit = self.lim.text()
        self.message = self.lineEdit_2.text()
        self.i = 0
        time.sleep(5)

        while self.i < int(self.limit):
            pt.typewrite(self.message)
            pt.press("enter")
            self.i += 1


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#f2e900;\">Enter limit</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#f2e900;\">Enter Text</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">SPAM</span></p></body></html>"))

def spamm():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
spamm()