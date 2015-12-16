# coding: utf-8
from PyQt4 import QtGui, QtCore
import sys
__author__ = 'yorick'


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 400, 300)
        self.setWindowIcon(QtGui.QIcon('icons/main.png'))
        # create cache
        self.cache = ''
        # create button del
        self.btnde = QtGui.QPushButton('<-', self)
        self.btnde.setGeometry(350, 30, 50, 100)
        # create lineEdit
        self.lin = QtGui.QTextEdit('', self)
        self.lin.setGeometry(0, 30, 350, 100)
        # create buttons numerick
        self.btn1 = QtGui.QPushButton('1', self)
        self.btn1.setGeometry(0, 140, 50, 35)
        self.btn2 = QtGui.QPushButton('2', self)
        self.btn2.setGeometry(50, 140, 50, 35)
        self.btn3 = QtGui.QPushButton('3', self)
        self.btn3.setGeometry(100, 140, 50, 35)
        self.btn4 = QtGui.QPushButton('4', self)
        self.btn4.setGeometry(150, 140, 50, 35)
        self.btn5 = QtGui.QPushButton('5', self)
        self.btn5.setGeometry(0, 180, 50, 35)
        self.btn6 = QtGui.QPushButton('6', self)
        self.btn6.setGeometry(50, 180, 50, 35)
        self.btn7 = QtGui.QPushButton('7', self)
        self.btn7.setGeometry(100, 180, 50, 35)
        self.btn8 = QtGui.QPushButton('8', self)
        self.btn8.setGeometry(150, 180, 50, 35)
        self.btn9 = QtGui.QPushButton('9', self)
        self.btn9.setGeometry(0, 220, 50, 35)
        self.btn0 = QtGui.QPushButton('0', self)
        self.btn0.setGeometry(50, 220, 50, 35)
        self.btnzap = QtGui.QPushButton(',', self)
        self.btnzap.setGeometry(100, 220, 100, 35)
        self.btnl = QtGui.QPushButton('(', self)
        self.btnl.setGeometry(0, 260, 100, 35)
        self.btnr = QtGui.QPushButton(')', self)
        self.btnr.setGeometry(100, 260, 100, 35)
        # create buttons calculate
        self.btnplus = QtGui.QPushButton('+', self)
        self.btnplus.setGeometry(200, 140, 100, 35)
        self.btnmin = QtGui.QPushButton('-', self)
        self.btnmin.setGeometry(300, 140, 100, 35)
        self.btndel = QtGui.QPushButton('/', self)
        self.btndel.setGeometry(200, 180, 100, 35)
        self.btnumn = QtGui.QPushButton('*', self)
        self.btnumn.setGeometry(300, 180, 100, 35)
        self.btnstep = QtGui.QPushButton('^', self)
        self.btnstep.setGeometry(200, 220, 100, 35)
        self.btnrav = QtGui.QPushButton('=', self)
        self.btnrav.setGeometry(200, 260, 200, 35)
        self.btnost = QtGui.QPushButton('//', self)
        self.btnost.setGeometry(300, 220, 100, 35)
        # create action on menu
        self.history = QtGui.QAction(QtGui.QIcon('icons/history.png'), 'History', self)
        self.history.setShortcut('Ctrl+h')
        self.history.setStatusTip('Calculating history')
        self.clh = QtGui.QAction('Clear history', self)
        self.clh.setShortcut('Ctrl+h+c')
        self.exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+e')
        self.exit.setStatusTip('Exit on application')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.menub = self.menuBar()
        mein = self.menub.addMenu('&Main')
        mein.addAction(self.history)
        mein.addAction(self.clh)
        mein.addAction(self.exit)

        # installing connects
        self.connect(self.btn0, QtCore.SIGNAL('clicked()'), self.but0)
        self.connect(self.btn1, QtCore.SIGNAL('clicked()'), self.but1)
        self.connect(self.btn2, QtCore.SIGNAL('clicked()'), self.but2)
        self.connect(self.btn3, QtCore.SIGNAL('clicked()'), self.but3)
        self.connect(self.btn4, QtCore.SIGNAL('clicked()'), self.but4)
        self.connect(self.btn5, QtCore.SIGNAL('clicked()'), self.but5)
        self.connect(self.btn6, QtCore.SIGNAL('clicked()'), self.but6)
        self.connect(self.btn7, QtCore.SIGNAL('clicked()'), self.but7)
        self.connect(self.btn8, QtCore.SIGNAL('clicked()'), self.but8)
        self.connect(self.btn9, QtCore.SIGNAL('clicked()'), self.but9)
        self.connect(self.btnplus, QtCore.SIGNAL('clicked()'), self.plus)
        self.connect(self.btnmin, QtCore.SIGNAL('clicked()'), self.minus)
        self.connect(self.btndel, QtCore.SIGNAL('clicked()'), self.delit)
        self.connect(self.btnost, QtCore.SIGNAL('clicked()'), self.deiost)
        self.connect(self.btnumn, QtCore.SIGNAL('clicked()'), self.umn)
        self.connect(self.btnr, QtCore.SIGNAL('clicked()'), self.r)
        self.connect(self.btnl, QtCore.SIGNAL('clicked()'), self.l)
        self.connect(self.btnde, QtCore.SIGNAL('clicked()'), self.de)
        self.connect(self.btnrav, QtCore.SIGNAL('clicked()'), self.calculate)
        self.connect(self.history, QtCore.SIGNAL('triggered()'), self.viewcache)
        self.connect(self.lin, QtCore.SIGNAL('selectionChanged()'), self.clear)
        self.connect(self.btnzap, QtCore.SIGNAL('clicked()'), self.zap)
        self.connect(self.btnstep, QtCore.SIGNAL('clicked()'), self.step)
        self.connect(self.clh, QtCore.SIGNAL('triggered()'), self.cl)

    def plus(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            text += '+'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '+'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '+'
            else:
                text = text[0:len(text) - 1] + '+'
        self.lin.setText(text)

    def minus(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            text += '-'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '-'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '-'
            else:
                text = text[0:len(text) - 1] + '-'
        self.lin.setText(text)

    def delit(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            if text[0:] == '0':
                pass
            else:
                text += '/'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '/'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '/'
            else:
                text = text[0:len(text) - 1] + '/'
        self.lin.setText(text)

    def umn(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            text += '*'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '*'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '*'
            else:
                text = text[0:len(text) - 1] + '*'
        self.lin.setText(text)

    def deiost(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            if text[0:] == '0':
                pass
            else:
                text += '//'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '//'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '//'
            else:
                text = text[0:len(text) - 1] + '//'
        self.lin.setText(text)

    def zap(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            text += '.'
        self.lin.setText(text)

    def step(self):
        text = self.lin.toPlainText()
        if len(text) == 0:
            pass
        elif text[len(text) - 1:len(text)].isalnum():
            text += '^'
        elif not text[len(text) - 1:len(text)].isalnum():
            if text[len(text) - 1:len(text)] == ')':
                text += '^'
            elif not text[len(text) - 2:len(text) - 1].isalnum():
                text = text[0:len(text) - 2] + '^'
            else:
                text = text[0:len(text) - 1] + '^'
        self.lin.setText(text)

    def but1(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*1'
        else:
            text += '1'
        self.lin.setText(text)

    def but2(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*2'
        else:
            text += '2'
        self.lin.setText(text)

    def but3(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*3'
        else:
            text += '3'
        self.lin.setText(text)

    def but4(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*4'
        else:
            text += '4'
        self.lin.setText(text)

    def but5(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*5'
        else:
            text += '5'
        self.lin.setText(text)

    def but6(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*6'
        else:
            text += '6'
        self.lin.setText(text)

    def but7(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*7'
        else:
            text += '7'
        self.lin.setText(text)

    def but8(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*8'
        else:
            text += '8'
        self.lin.setText(text)

    def but9(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == ')':
            text += '*9'
        else:
            text += '9'
        self.lin.setText(text)

    def but0(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == '/' or text[len(text) - 2:len(text)] == '//':
            pass
        else:
            if text[len(text) - 1:len(text)] == ')':
                text += '*0'
            else:
                text += '0'
        self.lin.setText(text)

    def r(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)] == '(':
            pass
        elif text.find('(') == -1:
            text = '(' + text + ')'
        else:
            text += ')'
        self.lin.setText(text)

    def l(self):
        text = self.lin.toPlainText()
        if text[len(text) - 1:len(text)].isnumeric():
            text += '*('
        else:
            text += '('
        self.lin.setText(text)

    def de(self):
        text = self.lin.toPlainText()
        text = text[0:len(text) - 1]
        self.lin.setText(text)

    def calculate(self):
        text = self.lin.toPlainText()
        if text.replace(' ', '') == '':
            pass
        else:
            try:
                t1 = text.replace('//', '%')
                t1 = t1.replace('^', '**')
                a = eval(t1)
                self.lin.setText(str(a))
                self.cache += text + '=' + str(a) + '\n'
            except:
                a = text + '=' + 'EROR'
                self.lin.setText(a)
                self.cache += text + '=' + str(a) + '\n'

    def viewcache(self):
        self.lin.setText(self.cache)

    def cl(self):
        if self.lin.toPlainText() == self.cache:
            self.lin.setText('')
            self.cache = ''
        else:
            self.cache = ''

    def clear(self):
        self.lin.setText('')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_0:
            self.but0()
        if e.key() == QtCore.Qt.Key_1:
            self.but1()
        if e.key() == QtCore.Qt.Key_2:
            self.but2()
        if e.key() == QtCore.Qt.Key_3:
            self.but3()
        if e.key() == QtCore.Qt.Key_4:
            self.but4()
        if e.key() == QtCore.Qt.Key_5:
            self.but5()
        if e.key() == QtCore.Qt.Key_6:
            self.but6()
        if e.key() == QtCore.Qt.Key_7:
            self.but7()
        if e.key() == QtCore.Qt.Key_8:
            self.but8()
        if e.key() == QtCore.Qt.Key_9:
            self.but9()
        if e.key() == QtCore.Qt.Key_Plus:
            self.plus()
        if e.key() == QtCore.Qt.Key_Minus:
            self.minus()
        if e.key() == QtCore.Qt.Key_Enter:
            self.calculate()
        if e.key() == QtCore.Qt.Key_Backspace:
            self.de()


def main():
    app = QtGui.QApplication(sys.argv)
    ma = Main()
    ma.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
