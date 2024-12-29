import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口的标题和大小
        self.setWindowTitle('PySide2 Button Example')
        self.setGeometry(100, 100, 300, 200)

        # 创建一个按钮并设置按钮的文本
        self.button = QPushButton('点击我', self)

        # 设置按钮的位置和大小
        self.button.setGeometry(100, 80, 100, 40)

        # 连接按钮的点击事件
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        # 当按钮被点击时调用这个方法
        print('按钮被点击了！14444445556667788997777gsq2.1ggg11144445558888')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec())
