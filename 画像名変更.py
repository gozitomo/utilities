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
#フォルダ内画像のを連番でリネームする
import os
import glob

path = r"\\192.168.1.55\ai-work\30.アノテーション作業用\保安具\（テスト用）シールド付ヘルメット画像"
img_list = sorted([f for f in os.listdir(path) if f.endswith(".jpg") or f.endswith(".jfif")])

print(img_list)
i = 1
for img in img_list:
    old_path = os.path.join(path, img)
    new_name = "gc_web_" + str(i).zfill(4) + ".jpg"
    new_path = os.path.join(path, new_name)
    
    os.rename(old_path, new_path)
    i += 1

# %%
