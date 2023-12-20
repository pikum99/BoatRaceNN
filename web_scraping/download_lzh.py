from time import sleep
from requests import get
from datetime import datetime as dt
from datetime import timedelta as td
from os import makedirs


def _get_date_list(START_DATE, END_DATE, SAVE_DIR):
    '''
    datalistを返す関数
    '''
    # ファイルを格納するフォルダを作成
    makedirs(SAVE_DIR, exist_ok=True)

    # 開始日と終了日を日付型に変換して格納
    start_date = dt.strptime(START_DATE, '%Y-%m-%d')
    end_date = dt.strptime(END_DATE, '%Y-%m-%d')
    # 日付の差から期間を計算
    days_num = (end_date - start_date).days + 1
    # 日付リストを格納する変数
    date_list = []

    # 日付リストを生成
    for i in range(days_num):
        # 開始日から日付を順に取得
        target_date = start_date + td(days=i)
        # 日付型を文字列に変換してリストに格納(YYYYMMDD)
        date_list.append(target_date.strftime("%Y%m%d"))

    return date_list


def _download_lzh_file(date_list, SAVE_DIR, INTERVAL, FIXED_URL):
    '''
    webからlzh_fileをダウンロードする関数
    URL生成とダウンロード
    '''
    def generate_url(date):
        '''
        urlとfile_nameを生成する関数
        '''
        yyyymm = date[0:4] + date[4:6]
        yymmdd = date[2:4] + date[4:6] + date[6:8]
        variable_url = FIXED_URL + yyyymm + "/k" + yymmdd + ".lzh"
        file_name = "k" + yymmdd + ".lzh"
        return variable_url, file_name

    # 処理ここから
    for date in date_list:
        variable_url, file_name = generate_url(date)
        r = get(variable_url)

        # レスポンスコードで分岐
        if r.status_code == 200:
            f = open(SAVE_DIR + file_name, 'wb')
            f.write(r.content)
            f.close()
            print(variable_url + " をダウンロードしました")
        else:
            print(variable_url + " のダウンロードに失敗しました")
        # 指定した間隔をあける
        sleep(INTERVAL)


if __name__ == "__main__":
    '''
    lzhファイルをダウンロードするpy
    '''
    # 開始日と終了日を指定(YYYY-MM-DD)
    START_DATE = "2022-01-01"
    END_DATE = "2023-06-01"
    # ファイルの保存先を指定
    SAVE_DIR = "./web_scraping/results_lzh/"
    # リクエスト間隔を指定(秒)　※サーバに負荷をかけないよう3秒以上を推奨
    INTERVAL = 3
    # URLの固定部分を指定
    FIXED_URL = "http://www1.mbrace.or.jp/od2/K/"

    data_list = _get_date_list(START_DATE, END_DATE, SAVE_DIR)
    _download_lzh_file(data_list, SAVE_DIR, INTERVAL, FIXED_URL)
