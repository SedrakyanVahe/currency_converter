import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
  def __init__(self):
    super(CurrencyConv, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.init_UI()

  def init_UI(self):
    self.setWindowTitle("CURRENCY CONVERTER")
    self.ui.input_currency.setPlaceholderText("FROM")
    self.ui.input_amount.setPlaceholderText("HOW MUCH")
    self.ui.output_currency.setPlaceholderText("TO")
    self.ui.output_amount.setPlaceholderText("RESULT")
    self.ui.pushButton.clicked.connect(self.converter)
    self.ui.info_button.clicked.connect(self.get_all_currencies)

  def converter(self):
    c = CurrencyConverter()

    try:
      input_currency = self.ui.input_currency.text()
      output_currency = self.ui.output_currency.text()
      input_amount = int(self.ui.input_amount.text())

      output_amount = round(c.convert(
        input_amount,
        "%s" % (input_currency.upper()),
        "%s" % (output_currency.upper()),
      ), 2, )

      self.ui.output_amount.setText(str(output_amount))

    except BaseException:
      error_msg = QMessageBox()
      error_msg.setIcon(QMessageBox.Critical)
      error_msg.setInformativeText("CURRENCY NOT FOUND!")
      error_msg.setWindowTitle("Error")
      error_msg.exec_()

  def get_all_currencies(self):
    c = CurrencyConverter()
    msg = QMessageBox()
    msg.setStyleSheet("QMessageBox{font-size:18px;\nbackground-color: #7cf4f2;}")
    msg.setWindowTitle("All currencies")
    msg.setText(str(c.currencies))
    msg.exec()

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
sys.exit(app.exec())