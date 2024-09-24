import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
class Harbili_Hesap_Makinesi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Harbili Hesap Makinesi')
        self.setGeometry(131, 131, 331, 531)

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.display = QLineEdit()
        vbox.addWidget(self.display)

        grid = QGridLayout()
        vbox.addLayout(grid)
        buttons = [
            'YAZILARI SIL RRRAAA', '1', '2', '3', 
            '4', '5', '6', '/', 
            '7', '8', '9', '*', 
            '0', '.', '=', '+', 
            '-'
        ] 
        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, button in zip(positions, buttons):
            btn = QPushButton(button)
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, *position)
    def on_click(self):
            sender = self.sender()
            text = sender.text()
            if text == 'YAZILARI SIL RRRAAA':
                self.display.clear()
            elif text == '=':
                try:
                    result = str(eval(self.display.text()))
                    self.display.setText(result)
                except ZeroDivisionError:
                    self.display.setText('0a bölme')
                except Exception as e:
                    self.display.setText('Hata: ' + str(e))
            else:
                self.display.setText(self.display.text() + text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Harbili_Hesap_Makinesi()
    calc.show()
    sys.exit(app.exec_())               