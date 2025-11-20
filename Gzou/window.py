# 実装すること
# PiSide6を使用してウィンドウを作成し、ボタンを横並びに2つ配置する
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import sys
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("横並びのボタン")
        # ウィンドウのサイズを設定
        # ウィンドウを中心に配置
        self.resize(300, 100)
        

        # レイアウトを作成
        layout = QHBoxLayout()

        # ボタンを作成
        button1 = QPushButton("キャプチャーボタン")
        button2 = QPushButton("白黒変換ボタン")

        # ボタンをレイアウトに追加
        layout.addWidget(button1)
        layout.addWidget(button2)

        # ウィンドウにレイアウトを設定
        self.setLayout(layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())