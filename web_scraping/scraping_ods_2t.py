import csv
import os
from time import sleep

from bs4 import BeautifulSoup
from requests import get
from datetime import datetime


def get_odds(target_url):
    '''
    Webサイトからオッズデータを抽出する関数 get_odds を定義
    '''
    # BeautifulSoupにWebサイトのコンテンツを渡す
    html = get(target_url)
    soup = BeautifulSoup(html.content, 'html.parser')
    # Webサイトからコピーしたcss selectorを貼り付け　※3連単と2連単は同じ
    target_table_selector = \
        "body > main > div > div > div > div.contentsFrame1_inner > div:nth-child(7) > table"
    # css selectorで指定したHTMLタグの中身を取得
    odds_table = soup.select_one(target_table_selector)
    # オッズデータがあった場合
    try:
        odds_table_elements = odds_table.select_one("tbody")
        row_list = odds_table_elements.select("tr")
        csv_row = []
        for row in row_list:
            for cell in row.select("td.oddsPoint"):
                csv_row.append(cell.get_text())
        res = ','.join(csv_row)
    except Exception:
        res = "No data"

    return res


# 開始合図
print("作業を開始します")

# レースコードが格納されているCSVファイルを指定　※最初の列に格納されていること
RACECODE_FILE_PATH = "./web_scraping/race_base_infomation/race_base_infomation_v1_1.csv"
# オッズデータを格納するCSVファイルの保存先を指定
ODDS_FILE_DIR = "./web_scraping/odds_infomation/"
# オッズデータを格納するCSVファイルの名前を指定
ODDS_FILE_NAME = "odds_race_base_infomation_v1_1.csv"
# オッズデータを格納するCSVファイルのヘッダーを指定
ODDS_FILE_HEADER = "レースコード,\
2連単_1-2,2連単_2-1,2連単_3-1,2連単_4-1,2連単_5-1,2連単_6-1,\
2連単_1-3,2連単_2-3,2連単_3-2,2連単_4-2,2連単_5-2,2連単_6-2,\
2連単_1-4,2連単_2-4,2連単_3-4,2連単_4-3,2連単_5-3,2連単_6-3,\
2連単_1-5,2連単_2-5,2連単_3-5,2連単_4-5,2連単_5-4,2連単_6-4,\
2連単_1-6,2連単_2-6,2連単_3-6,2連単_4-6,2連単_5-6,2連単_6-5\n"
# URLの固定部分を指定
FIXED_URL = "https://www.boatrace.jp/owpc/pc/race/odds"
# 舟券種別を指定
BET_TYPE = "2tf"
# リクエスト間隔を指定(秒)　※サーバに負荷をかけないよう3秒以上を推奨
INTERVAL = 3

os.makedirs(ODDS_FILE_DIR, exist_ok=True)

# オッズデータを格納するCSVファイルを作成しヘッダ情報を書き込む
with open(ODDS_FILE_DIR + ODDS_FILE_NAME, "w", encoding="utf_8") as csv_file:
    csv_file.write(ODDS_FILE_HEADER)
    # 先頭にwithを記載しているのでclose( )関数の処理は不要
    csv_file.close()

# レースコードを取得してURLを生成しオッズデータを取得
with open(RACECODE_FILE_PATH, "r", encoding="utf_8") as race_code_file:
    reader = csv.reader(race_code_file)
    # ヘッダー行をスキップ
    header = next(reader)
    # レースコードを取得するCSVファイルを1行ずつ読み込む
    for row in reader:
        # 最初の列(レースコード)を格納
        race_code = row
        # 3レターコードと場コードの対応表
        dict_stadium = {
            '桐生': '01',
            '戸田': '02',
            '江戸川': '03',
            '平和島': '04',
            '多摩川': '05',
            '浜名湖': '06',
            '蒲郡': '07',
            '常滑': '08',
            '津': '09',
            '三国': '10',
            'びわこ': '11',
            '琵琶湖': '11',
            '住之江': '12',
            '尼崎': '13',
            '鳴門': '14',
            '丸亀': '15',
            '児島': '16',
            '宮島': '17',
            '徳山': '18',
            '下関': '19',
            '若松': '20',
            '芦屋': '21',
            '福岡': '22',
            '唐津': '23',
            '大村': '24'
        }

        # レースコードからレース回・レース場(場コード)・レース日を取得
        race_round = race_code[4][:-1]
        stadium_code = dict_stadium[race_code[3]]
        # 元の文字列を定義
        original_string = race_code[2]
        # 元のフォーマットを指定
        original_format = "%Y/%m/%d"
        # 変換後のフォーマットを指定
        new_format = "%Y%m%d"
        # 元の文字列をdatetimeオブジェクトに変換
        date_object = datetime.strptime(original_string, original_format)
        # 新しいフォーマットに変換した文字列を取得
        date = date_object.strftime(new_format)
        # URLを生成
        target_url = FIXED_URL + BET_TYPE + "?rno=" + race_round + "&jcd=" + stadium_code + "&hd=" + date
        print(target_url + " からオッズデータを取得します")
        # 関数 get_odds にURLを渡しオッズデータを取得する
        odds_data = get_odds(target_url)
        # CSVファイルを追記モードで開き、レースコードとオッズデータを書き込む
        with open(ODDS_FILE_DIR + ODDS_FILE_NAME, "a", encoding="utf_8") as csv_file:
            csv_file.write(odds_data + "\n")
        # 指定した間隔をあける
        sleep(INTERVAL)

# 終了合図
print("作業を終了しました")
