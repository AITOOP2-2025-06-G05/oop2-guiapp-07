import cv2
from my_module.k24101kk.lecture05_camera_image_capture import MyVideoCapture


def cap_image(output_path="captured.png"):
    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()
    # 画像の取得
    capture_img: cv2.Mat = app.get_img()

    # 画像の保存、表示
    cv2.imwrite("captured.png",capture_img)
    cv2.imshow("Captured Image",capture_img)
    cv2.waitKey(0)