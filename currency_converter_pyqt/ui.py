from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setFixedWidth(480)
    MainWindow.setFixedHeight(900)
    font = QtGui.QFont()
    font.setFamily("URW Bookman")
    font.setPointSize(28)
    font.setBold(True)
    font.setWeight(75)
    MainWindow.setFont(font)
    MainWindow.setStyleSheet("background-color: #22222e")
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.frame = QtWidgets.QFrame(self.centralwidget)
    self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
    self.frame.setStyleSheet("background-color: #0657f9")
    self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.frame.setObjectName("frame")
    self.label = QtWidgets.QLabel(self.frame)
    self.label.setGeometry(QtCore.QRect(60, 0, 411, 51))
    font = QtGui.QFont()
    font.setFamily("Serif")
    font.setPointSize(28)
    font.setBold(True)
    font.setItalic(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setStyleSheet("color: white")
    self.label.setObjectName("label")
    self.label_2 = QtWidgets.QLabel(self.frame)
    self.label_2.setGeometry(QtCore.QRect(140, 60, 221, 201))
    self.label_2.setText("")
    self.label_2.setPixmap(QtGui.QPixmap("img/icon1.png"))
    self.label_2.setObjectName("label_2")
    self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
    self.input_currency.setGeometry(QtCore.QRect(50, 320, 380, 60))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.input_currency.setFont(font)
    self.input_currency.setStyleSheet(
      "background-color: #22222e;\n"
      "color: white;\n"
      "border: 2px solid #0657f9;\n"
      "border-radius:30;")
    self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
    self.input_currency.setObjectName("input_currency")
    self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
    self.input_amount.setGeometry(QtCore.QRect(50, 420, 380, 60))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.input_amount.setFont(font)
    self.input_amount.setStyleSheet(
      "background-color: #22222e;\n"
      "color: white;\n"
      "border: 2px solid #0657f9;\n"
      "border-radius:30;")
    self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
    self.input_amount.setObjectName("input_amount")
    self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
    self.output_currency.setGeometry(QtCore.QRect(50, 520, 380, 60))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.output_currency.setFont(font)
    self.output_currency.setStyleSheet(
      "background-color: #22222e;\n"
      "color: white;\n"
      "border: 2px solid #0657f9;\n"
      "border-radius:30;")
    self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
    self.output_currency.setObjectName("output_currency")
    self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
    self.output_amount.setGeometry(QtCore.QRect(50, 620, 380, 60))
    font = QtGui.QFont()
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.output_amount.setFont(font)
    self.output_amount.setStyleSheet(
      "background-color: #22222e;\n"
      "color: white;\n"
      "border: 2px solid #0657f9;\n"
      "border-radius:30;")
    self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
    self.output_amount.setObjectName("output_amount")
    self.pushButton = QtWidgets.QPushButton(self.centralwidget)
    self.pushButton.setGeometry(QtCore.QRect(50, 720, 380, 60))
    font = QtGui.QFont()
    font.setFamily("Ubuntu Condensed")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.pushButton.setFont(font)
    self.pushButton.setStyleSheet(
      "QPushButton{\n"
      "    color: white;\n"
      "    background-color: #06f94f;\n"
      "    border-radius: 30;\n"
      "}\n"
      "\n"
      "QPushButton:pressed{\n"
      "    background-color: #06e023;\n"
      "    \n"
      "}")
    self.pushButton.setObjectName("pushButton")
    MainWindow.setCentralWidget(self.centralwidget)
    self.info_button = QtWidgets.QPushButton(self.centralwidget)
    self.info_button.setGeometry(QtCore.QRect(50, 820, 380, 60))
    font.setFamily("Ubuntu Condensed")
    font.setPointSize(20)
    font.setBold(True)
    font.setWeight(75)
    self.info_button.setFont(font)
    self.info_button.setStyleSheet(
      "QPushButton{\n"
      "    color: white;\n"
      "    background-color: #ed4c2c;\n"
      "    border-radius: 30;\n"
      "}\n"
      "\n"
      "QPushButton:pressed{\n"
      "    background-color: #d33212;\n"
      "    \n"
      "}")
    self.info_button.setObjectName("info_button")
    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.label.setText(_translate("MainWindow", "currency converter"))
    self.input_currency.setText(_translate("MainWindow", ""))
    self.input_amount.setText(_translate("MainWindow", ""))
    self.output_currency.setText(_translate("MainWindow", ""))
    self.output_amount.setText(_translate("MainWindow", ""))
    self.pushButton.setText(_translate("MainWindow", "CONVERT"))
    self.info_button.setText(_translate("MainWindow", "ALL CURRENCIES"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())