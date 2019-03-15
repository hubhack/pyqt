import sys

try:
    import PyQt5
except ImportError:
    import tkinter
    from tkinter import messagebox
    err_str = "请安装PyQt5后再打开: pip indatll PyQ5"
    messagebox.showerror("模块错误",err_str)
    raise ImportError(err_str)
    sys.exit()


from random import randint
from PyQt5.QtWidgets import \
    QApplication,           \
    QWidget,                \
    QPushButton,            \
    QLCDNumber,\
    QDesktopWidget, \
    QMessageBox,\
from PyQt5.QtCore import Qt


