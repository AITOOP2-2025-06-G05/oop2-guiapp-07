import cv2
import os
import glob
from pathlib import Path


def grayscale_image(
    image_path: str, output_dir: str = "output_images", show_window: bool = False
):
    # ファイルの存在確認
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"エラー: 画像ファイルが見つかりません - {image_path}")

    # 画像を読み込む
    img = cv2.imread(image_path)

    # 画像の読み込みチェック
    if img is None:
        raise ValueError(f"エラー: 画像の読み込みに失敗しました - {image_path}")

    # グレースケール化
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 出力ディレクトリの作成（存在しない場合）
    os.makedirs(output_dir, exist_ok=True)

    # 出力ファイル名の生成
    input_filename = Path(image_path).stem
    input_extension = Path(image_path).suffix
    output_filename = f"{input_filename}_grayscale{input_extension}"
    output_path = os.path.join(output_dir, output_filename)

    # グレースケール画像を保存
    cv2.imwrite(output_path, gray_img)
    print(f"グレースケール画像を保存しました: {output_path}")

    # オプション: ウィンドウで表示
    if show_window:
        window_name = f"Grayscale - {input_filename}"
        cv2.imshow(window_name, gray_img)
        print("ウィンドウに表示しています。キーを押すと閉じます。")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return output_path


def process_png_images(output_dir: str = "output_images"):
    """
    プロジェクト直下のPNG画像ファイルを検索してグレースケール化する

    Args:
        output_dir: 出力ディレクトリのパス（デフォルト: "output_images"）

    Returns:
        tuple: (converted_files, error_message)
            converted_files: 変換に成功したファイルのリスト
            error_message: エラーメッセージ（エラーがない場合はNone）
    """
    # プロジェクト直下のPNG画像ファイルを検索
    image_files = glob.glob("*.png")

    # 画像が見つからない場合
    if not image_files:
        return [], "プロジェクト直下に画像ファイルが見つかりません。"

    # 見つかった画像を処理
    converted_files = []
    for image_path in image_files:
        try:
            output_path = grayscale_image(image_path, output_dir)
            converted_files.append(output_path)
        except (FileNotFoundError, ValueError) as e:
            print(f"スキップ: {image_path} - {str(e)}")
            continue

    if not converted_files:
        return [], "画像の変換に失敗しました。"

    return converted_files, None


def main():
    """
    メイン関数 - 画像ファイルをグレースケール化
    """
    # 処理する画像のパス
    image_paths = ["Gzou/images/google.png", "Gzou/images/camera_capture.png"]

    for image_path in image_paths:
        try:
            print(f"\n処理中: {image_path}")
            output_path = grayscale_image(
                image_path, "Gzou/output_images", show_window=True
            )
            print(f"完了: {output_path}\n")
        except (FileNotFoundError, ValueError) as e:
            print(e)
            continue
