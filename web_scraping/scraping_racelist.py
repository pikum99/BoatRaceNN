import csv
import os
from time import sleep

from bs4 import BeautifulSoup
from requests import get
from datetime import datetime
import re


def get_odds(target_url):
    '''
    Webサイトからレースデータを抽出する関数 get_odds を定義
    '''
    # BeautifulSoupにWebサイトのコンテンツを渡す
    html = get(target_url)
    soup = BeautifulSoup(html.content, 'html.parser')
    # Webサイトからコピーしたcss selectorを貼り付け　※3連単と2連単は同じ
    target_table_selector = \
        "body > main > div > div > div > div.contentsFrame1_inner > div.table1.is-tableFixed__3rdadd > table"
    # css selectorで指定したHTMLタグの中身を取得
    odds_table = soup.select_one(target_table_selector)
    # レースデータがあった場合
    try:
        # 1号艇
        result_list = []
        odds_table_elements = odds_table.select_one("tbody")
        row_list = odds_table_elements.select("td")
        csv_row = []
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)

        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        # 2号艇
        res = ''
        csv_row = []
        odds_table_elements = odds_table_elements.find_next_sibling()
        row_list = odds_table_elements.select("td")
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)
        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        # 3号艇
        res = ''
        csv_row = []
        odds_table_elements = odds_table_elements.find_next_sibling()
        row_list = odds_table_elements.select("td")
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)
        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        # 4号艇
        res = ''
        csv_row = []
        odds_table_elements = odds_table_elements.find_next_sibling()
        row_list = odds_table_elements.select("td")
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)
        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        # 5号艇
        res = ''
        csv_row = []
        odds_table_elements = odds_table_elements.find_next_sibling()
        row_list = odds_table_elements.select("td")
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)
        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        # 6号艇
        res = ''
        csv_row = []
        odds_table_elements = odds_table_elements.find_next_sibling()
        row_list = odds_table_elements.select("td")
        for row in row_list:
            text = row.get_text(strip=True)
            text = re.sub(r'\s+', '', text)
            if text:
                csv_row.append(text)
        race_number = csv_row[0]
        # 個人基本
        person_number = csv_row[1].split('/')[0]
        person_rank = csv_row[1].split('/')[1][:2]
        person_weight = csv_row[1].split('/')[3][:4]
        # 個人競技
        flying_num = csv_row[2][1:2]
        late_num = csv_row[2][3:4]
        start_time = csv_row[2][4:]
        # 勝率(全国)
        country_win_rate = csv_row[3][:4]
        country_win_rate_second = csv_row[3][4:9]
        country_win_rate_third = csv_row[3][9:]
        # 勝率(当地) 
        local_win_rate = csv_row[4][:4]
        local_win_rate_second = csv_row[4][4:9]
        local_win_rate_third = csv_row[4][9:]
        # 勝率(モーター)
        motor_win_rate = csv_row[5][:2]
        motor_win_rate_second = csv_row[5][2:7]
        motor_win_rate_third = csv_row[5][7:]
        # 勝率(ボート)
        boat_win_rate = csv_row[6][:2]
        boat_win_rate_second = csv_row[6][2:7]
        boat_win_rate_third = csv_row[6][7:]

        res = race_number + ',' + person_number + ',' + person_rank + ',' + person_weight + ',' \
            + flying_num + ',' + late_num + ',' + start_time + ',' \
            + country_win_rate + ',' + country_win_rate_second + ',' + country_win_rate_third + ',' \
            + local_win_rate + ',' + local_win_rate_second + ',' + local_win_rate_third + ',' \
            + motor_win_rate + ',' + motor_win_rate_second + ',' + motor_win_rate_third + ',' \
            + boat_win_rate + ',' + boat_win_rate_second + ',' + boat_win_rate_third
        result_list.append(res)

        result = ','.join(result_list)
    except Exception as e:
        print(e)
        result = "No data"

    return result


# 開始合図
print("作業を開始します")

# レースコードが格納されているCSVファイルを指定　※最初の列に格納されていること
RACECODE_FILE_PATH = "./web_scraping/race_base_infomation/race_base_infomation.csv"
# レースデータを格納するCSVファイルの保存先を指定
ODDS_FILE_DIR = "./web_scraping/racelist_infomation/"
# レースデータを格納するCSVファイルの名前を指定
ODDS_FILE_NAME = "racelist.csv"
# レースデータを格納するCSVファイルのヘッダーを指定
ODDS_FILE_HEADER = "レース番号_1,個人番号_1,ランク_1,体重_1,フライング_1,レイト_1,スタートタイム_1,全国勝率_1,全国2連率_1,\
全国3連率_1,当地勝率_1,当地2連率_1,当地3連率_1,モーター番号_1,モーター2連率_1,\
モーター3連率_1,モーター番号_1,モーター2連率_1,モーター3連率_1,レース番号_1,\
個人番号_2,ランク_2,体重_2,フライング_2,レイト_2,スタートタイム_2,\
全国勝率_2,全国2連率_2,全国3連率_2,当地勝率_2,当地2連率_2,当地3連率_2,モーター番号_2,\
モーター2連率_2,モーター3連率_2,モーター番号_2,モーター2連率_2,モーター3連率_2,レース番号_2,\
個人番号_3,ランク_3,体重_3,フライング_3,レイト_3,スタートタイム_3,全国勝率_3,全国2連率_3,全国3連率_3,当地勝率_3,当地2連率_3,当地3連率_3,\
モーター番号_3,モーター2連率_3,モーター3連率_3,モーター番号_3,モーター2連率_3,モーター3連率_3,レース番号_4,個人番号_4,ランク_4,体重_4,\
フライング_4,レイト_4,スタートタイム_4,全国勝率_4,全国2連率_4,全国3連率_4,当地勝率_4,当地2連率_4,当地3連率_4,モーター番号_4,モーター2連率_4,\
モーター3連率_4,モーター番号_4,モーター2連率_4,モーター3連率_4,レース番号_5,個人番号_5,ランク_5,体重_5,フライング_5,レイト_5,スタートタイム_5,全国勝率_5,\
全国2連率_5,全国3連率_5,当地勝率_5,当地2連率_5,当地3連率_5,モーター番号_5,モーター2連率_5,モーター3連率_5,モーター番号_5,モーター2連率_5,モーター3連率_5,\
レース番号_6,個人番号_6,ランク_6,体重_6,フライング_6,レイト_6,スタートタイム_6,全国勝率_6,全国2連率_6,全国3連率_6,当地勝率_6,当地2連率_6,当地3連率_6,モーター番号_6,\
モーター2連率_6,モーター3連率_6,モーター番号_6,モーター2連率_6,モーター3連率_6\n"

# URLの固定部分を指定
FIXED_URL = "https://www.boatrace.jp/owpc/pc/race/racelist"

# 舟券種別を指定
BET_TYPE = "3t"
# リクエスト間隔を指定(秒)　※サーバに負荷をかけないよう3秒以上を推奨

INTERVAL = 0.5

os.makedirs(ODDS_FILE_DIR, exist_ok=True)

# レースデータを格納するCSVファイルを作成しヘッダ情報を書き込む
with open(ODDS_FILE_DIR + ODDS_FILE_NAME, "w", encoding="utf_8") as csv_file:
    csv_file.write(ODDS_FILE_HEADER)
    # 先頭にwithを記載しているのでclose( )関数の処理は不要
    csv_file.close()

# レースコードを取得してURLを生成しレースデータを取得
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
            '琵琶湖': '11',
            'びわこ': '11',
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

        target_url = FIXED_URL + "?rno=" + race_round + "&jcd=" + stadium_code + "&hd=" + date
        print(target_url + " からレースデータを取得します")
        # 関数 get_odds にURLを渡しレースデータを取得する
        try:
            odds_data = get_odds(target_url)
        except Exception:
            # 失敗した場合20分休憩
            sleep(1200)
            odds_data = get_odds(target_url)
        # CSVファイルを追記モードで開き、レースコードとレースを書き込む
        with open(ODDS_FILE_DIR + ODDS_FILE_NAME, "a", encoding="utf_8") as csv_file:
            csv_file.write(odds_data + "\n")
        # 指定した間隔をあける
        sleep(INTERVAL)

# 終了合図
print("作業を終了しました")
