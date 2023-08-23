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
import os
import glob

path = r"\\192.168.1.55\ai-work\30.アノテーション作業用\床面データセット\清水建設_岩塚物流センター（白ひび）\Annotations"
png_list = glob.glob(os.path.join(path, "*.png"))

for png in png_list:
    png_name = os.path.splitext(os.path.basename(png))[0]
    if "crack" in png_name.split("-")[-1] :
        pass
    else:
        new = png_name.split("-")[-1][:3] + "-crack" + png_name.split("-")[-1][3:] + ".png"
        name_parts = png_name.split("-")[:-1]
        name_parts.append(new)
        new_name = "-".join(name_parts)
        new_path = os.path.join(path, new_name)
        os.rename(png, new_path)
        
        print(new_path)

# %%
import os
import glob

path = r"\\192.168.1.55\ai-work\30.アノテーション作業用\床面データセット\20230810検出漏れ要修正\Annotations"
xml_list = glob.glob(os.path.join(path, "*.xml"))
for xml in xml_list:
    new_name = os.path.splitext(os.path.basename(xml))[0] + "-crack.png"
    new_path = os.path.join(path, new_name)
    print(new_name)
    os.rename(xml, new_path)

# %%
