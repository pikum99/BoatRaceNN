import re
import lhafile
import os


def unzip_lzh(lzh_file_list):
    for lzh_file_name in lzh_file_list:
        # 拡張子が lzh のファイルに対してのみ実行
        if re.search(".lzh", lzh_file_name):
            file = lhafile.Lhafile(LZH_FILE_DIR + lzh_file_name)
            # 解凍したファイルの名前を取得
            info = file.infolist()
            name = info[0].filename
            # 解凍したファイルの保存
            open(TXT_FILE_DIR + name, "wb").write(file.read(name))
            print(TXT_FILE_DIR + lzh_file_name + " を解凍しました")


if __name__ == "__main__":
    """
    LZHファイルをunzipするpyファイル
    """
    # ダウンロードしたLZHファイルが保存されている場所を指定
    LZH_FILE_DIR = "./web_scraping/results_lzh/"
    # 解凍したファイルを保存する場所を指定
    TXT_FILE_DIR = "./web_scraping/results_txt/"
    os.makedirs(TXT_FILE_DIR, exist_ok=True)
    lzh_file_list = os.listdir(LZH_FILE_DIR)
    unzip_lzh(lzh_file_list)
