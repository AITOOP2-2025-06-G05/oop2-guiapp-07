# 実装すること
# PiSide6を使用してウィンドウを作成し、ボタンを横並びに2つ配置する
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
)
import sys
from src.grayscale import process_png_images

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("横並びのボタン")
        # ウィンドウのサイズを設定
        # ウィンドウを中心に配置
        self.resize(300, 100)

        # キャプチャした画像のパスを保持
        self.captured_image_path = "output_images/camera_capture.png"

        # レイアウトを作成
        layout = QHBoxLayout()

        # ボタンを作成
        button1 = QPushButton("キャプチャーボタン")
        button2 = QPushButton("白黒変換ボタン")

        # ボタンにイベントハンドラを接続
        button2.clicked.connect(self.convert_grayscale)

        # ボタンをレイアウトに追加
        layout.addWidget(button1)
        layout.addWidget(button2)

        # ウィンドウにレイアウトを設定
        self.setLayout(layout)

    def convert_grayscale(self):
        """画像をグレースケール化する"""
        try:
            # グレースケール処理を実行
            converted_files, error_message = process_png_images("output_images")

            # エラーがある場合
            if error_message:
                QMessageBox.warning(self, "エラー", error_message)
                return

            # 成功した場合
            file_list = "\n".join(converted_files)
            QMessageBox.information(
                self,
                "成功",
                f"グレースケール変換が完了しました。\n\n変換された画像:\n{file_list}",
            )

        except Exception as e:
            QMessageBox.critical(
                self, "エラー", f"グレースケール変換中にエラーが発生しました:\n{str(e)}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
