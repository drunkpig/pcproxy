"""
实现qt类装饰器，具备功能：
1，作用在类上能够自动在构建类之后调用 QtCore.QMetaObject.connectSlotsByName(self)
2，扫描

"""
import sys

from PySide2 import QtCore
from PySide2.QtWidgets import QDialog, QVBoxLayout, QPushButton, QApplication


def autowire(clz):
    def auto_wire(*args, **kwargs):
        obj = clz(*args, **kwargs)
        QtCore.QMetaObject.connectSlotsByName(obj)
        return obj
    return auto_wire


@autowire
class UIMyEditorDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.__setup_ui()

    def __setup_ui(self):
        layout = QVBoxLayout()
        self.btn = QPushButton("click me")
        self.btn.setObjectName("btn")
        layout.addWidget(self.btn)
        self.setLayout(layout)



class MyEditorDialog(UIMyEditorDialog):
    def __init__(self, parent):
        super().__init__(parent)

    @QtCore.Slot()
    def on_btn_clicked(self):
        print("clicked")


if __name__=="__main__":
    qtapp = QApplication(sys.argv)
    dialog = MyEditorDialog(None)
    dialog.show()
    qtapp.exec_()

