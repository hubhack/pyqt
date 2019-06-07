import tkinter
import os
import tkinter.font as tkfont
class Window(object):
    def __init__(self):
        self.tk = tkinter.Tk()
        # 设置字体
        self.sysfont = tkfont.Font(self.tk, size = 28)

        self.tk = tkinter.Tk()
        self.tk.title('hah')
        self.label = tkinter.Label(master=self.tk, text = 'myname')
        self.label.pack()

        self.entry = tkinter.Entry(master=self.tk)
        self.entry.pack()

        self.button = tkinter.Button(master = self.tk, text = '提交')
        self.button.pack()
        self.tk.mainloop()
    def sayhello(self):
        pass
win = Window()
