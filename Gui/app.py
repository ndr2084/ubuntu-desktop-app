from Controller.app_controller import AppService, AppController
from Repo.app_repo import AppRepo
from Service.app_service import AppService

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui



class MyWidget(QtWidgets.QWidget):
    repo = AppRepo()
    service = AppService(repo)
    controller = AppController(service)
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
        self.controller.open_application('pycharm')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

