import csv

def merge_csv(file1, file2, output_file):
    # ファイル1を読み込む
    with open(file1, 'r', encoding="utf-8") as f1:
        reader1 = csv.reader(f1)
        data1 = list(reader1)

    # ファイル2を読み込む
    with open(file2, 'r', encoding="utf-8") as f2:
        reader2 = csv.reader(f2)
        data2 = list(reader2)

    # 2つのデータを結合する
    merged_data = []
    for row1, row2 in zip(data1, data2):
        merged_row = row1 + row2
        merged_data.append(merged_row)

    # 出力ファイルに結果を書き込む
    with open(output_file, 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(merged_data)

    print("CSVファイルの結合が完了しました。")


if __name__ == "__main__":
    """
    二つのcsvを結合させるpyファイル
    """
    # 2つの入力ファイルと出力ファイルのパスを指定して実行

    merge_csv('./web_scraping/race_base_infomation/race_base_infomation_2.csv', './web_scraping/racelist_infomation/racelist_2.csv', './web_scraping/dataset_v2.csv')
