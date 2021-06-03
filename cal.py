import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.v_box = QVBoxLayout()
        self.h_box1 = QHBoxLayout() 
        self.h_box2 = QHBoxLayout() 
        self.h_box3 = QHBoxLayout() 
        self.h_box4 = QHBoxLayout() 

        self.lbl_answer = QLabel()

        self.btn_0 = QPushButton("0")
        self.btn_1 = QPushButton("1")
        self.btn_2 = QPushButton("2")
        self.btn_3 = QPushButton("3")
        self.btn_4 = QPushButton("4")
        self.btn_5 = QPushButton("5")
        self.btn_6 = QPushButton("6")
        self.btn_7 = QPushButton("7")
        self.btn_8 = QPushButton("8")
        self.btn_9 = QPushButton("9")

        self.btn_clear = QPushButton("CA")
        self.btn_plus = QPushButton("+")
        self.btn_minus = QPushButton("-")
        self.btn_mul = QPushButton("*")
        self.btn_div = QPushButton("/")
        self.btn_equal = QPushButton("=")

        self.h_box1.addWidget(self.btn_7)
        self.h_box1.addWidget(self.btn_8)
        self.h_box1.addWidget(self.btn_9)
        self.h_box1.addWidget(self.btn_div)

        self.h_box2.addWidget(self.btn_4)
        self.h_box2.addWidget(self.btn_5)
        self.h_box2.addWidget(self.btn_6)
        self.h_box2.addWidget(self.btn_mul)

        self.h_box3.addWidget(self.btn_1)
        self.h_box3.addWidget(self.btn_2)
        self.h_box3.addWidget(self.btn_3)
        self.h_box3.addWidget(self.btn_minus)

        self.h_box4.addWidget(self.btn_clear)
        self.h_box4.addWidget(self.btn_0)
        self.h_box4.addWidget(self.btn_equal)
        self.h_box4.addWidget(self.btn_plus)

        self.v_box.addWidget(self.lbl_answer)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2) 
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.btn_0.clicked.connect(lambda: self.pressed_number("0"))
        self.btn_1.clicked.connect(lambda: self.pressed_number("1"))
        self.btn_2.clicked.connect(lambda: self.pressed_number("2"))
        self.btn_3.clicked.connect(lambda: self.pressed_number("3"))
        self.btn_4.clicked.connect(lambda: self.pressed_number("4"))
        self.btn_5.clicked.connect(lambda: self.pressed_number("5"))
        self.btn_6.clicked.connect(lambda: self.pressed_number("6"))
        self.btn_7.clicked.connect(lambda: self.pressed_number("7"))
        self.btn_8.clicked.connect(lambda: self.pressed_number("8"))
        self.btn_9.clicked.connect(lambda: self.pressed_number("9"))
        self.btn_plus.clicked.connect(lambda: self.pressed_operation("+"))
        self.btn_minus.clicked.connect(lambda: self.pressed_operation("-"))
        self.btn_mul.clicked.connect(lambda: self.pressed_operation("*"))
        self.btn_div.clicked.connect(lambda: self.pressed_operation("/"))  
        self.btn_equal.clicked.connect(self.calculate)
        self.btn_clear.clicked.connect(self.clear)

        self.setLayout(self.v_box)

    def pressed_number(self, number):
        self.lbl_answer.setText(self.lbl_answer.text() + number)

    def pressed_operation(self, operation):
        if not self.lbl_answer.text() == "":
            self.lbl_answer.setText(self.lbl_answer.text() + operation)

    def calculate(self):
        equation = self.lbl_answer.text()
        self.lbl_answer.setText(str(eval(equation)))
    
    def clear(self):
        equation = self.lbl_answer.text()
        self.lbl_answer.setText(equation[:-1])   
        
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_0:
            self.pressed_number("0") 
        elif event.key() == Qt.Key_1:
            self.pressed_number("1")  
        elif event.key() == Qt.Key_2:
            self.pressed_number("2")
        elif event.key() == Qt.Key_3:
            self.pressed_number("3")
        elif event.key() == Qt.Key_4:
            self.pressed_number("4")
        elif event.key() == Qt.Key_5:
            self.pressed_number("5")
        elif event.key() == Qt.Key_6:
            self.pressed_number("6")
        elif event.key() == Qt.Key_7:
            self.pressed_number("7")
        elif event.key() == Qt.Key_8:
            self.pressed_number("8")
        elif event.key() == Qt.Key_9:
            self.pressed_number("9")
        elif event.key() == Qt.Key_Backspace:
            self.clear()
        elif event.key() == Qt.Key_Plus:
            self.pressed_number("+")
        elif event.key() == Qt.Key_Minus:
            self.pressed_number("-")
        elif event.key() == Qt.Key_Equal:
            self.calculate()

app = QApplication(sys.argv)
win = Calculator()
import os
# os.system(sys.argv[1])
win.show()
app.exec_()










