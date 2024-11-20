import matplotlib.font_manager as fm
import os

# ttcファイルのフォント一覧を表示する
font_path = 'ipam.ttc'  # フォントファイルのパス

# ttcファイルからフォントをリストアップ
font_files = fm.findSystemFonts(fontpaths=[font_path], fontext='ttc')

# フォントファミリ名を表示
print("Fonts in the TTC file:")
for font_file in font_files:
    font = fm.FontProperties(fname=font_file)
    print(font.get_name())

