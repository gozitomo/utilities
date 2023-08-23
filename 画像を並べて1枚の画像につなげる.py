# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from PIL import Image
import os

# 画像が格納されているフォルダのパス
folder_path = r"\\192.168.1.55\ai-work\25.学習データセット\保安具\NO08_20230816\results\on_safety_face_shield\JPEGImages\3"

# 画像ファイル名のリストを取得
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")])
print(image_files)

# 1行あたりの画像数と1列あたりの画像数
images_per_row = 10
images_per_column = 6

# 画像の幅と高さ
image_width = 480  # 各画像の幅
image_height = 640  # 各画像の高さ

# 出力画像のサイズ
output_width = image_width * images_per_row
output_height = image_height * images_per_column

# 空の出力画像を作成
output_image = Image.new("RGB", (output_width, output_height))

# 画像を結合して出力画像に貼り付け
for i in range(images_per_column):
    for j in range(images_per_row):
        index = i * images_per_row + j
        if index < len(image_files):
            image_path = os.path.join(folder_path, image_files[index])
            img = Image.open(image_path)
            output_image.paste(img, (j * image_width, i * image_height))


# 出力画像を保存
output_image.save(os.path.join(folder_path, "output_image.jpg"))

print("画像の結合が完了し、output_image.jpgとして保存されました。")

# %%
