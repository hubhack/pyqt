if __name__ == "__main__":
    app  = QApplication(sys.argv)


    w = QWidget()
    w.resize(250,150)
    w.move(300,300)
    w,setWidowTitle('简单')
    w.show()
    sys.exit(app.exec())