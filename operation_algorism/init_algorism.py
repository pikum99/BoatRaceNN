# -*- coding: utf-8 -*-
"""BUGProject運用.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TGUqspLw5-a7IDoUYSZJ-VQIDrFm734z
"""

import pandas as pd

res_dict = {
    '1-2': 0,
    '1-3': 1,
    '1-4': 2,
    '1-5': 3,
    '1-6': 4,
    '2-1': 5,
    '2-3': 6,
    '2-4': 7,
    '2-5': 8,
    '2-6': 9,
    '3-1': 10,
    '3-2': 11,
    '3-4': 12,
    '3-5': 13,
    '3-6': 14,
    '4-1': 15,
    '4-2': 16,
    '4-3': 17,
    '4-5': 18,
    '4-6': 19,
    '5-1': 20,
    '5-2': 21,
    '5-3': 22,
    '5-4': 23,
    '5-6': 24,
    '6-1': 25,
    '6-2': 26,
    '6-3': 27,
    '6-4': 28,
    '6-5': 29
}

"""各csvについては、開発者に連絡してください。

ダウンロードして、右のフォルダアイコンをクリックして、sample_dataの隣に入れてください
"""

odds_df = pd.read_csv('/content/odds_race_base_infomation_v1_1.csv')
ai_prod_df = pd.read_csv('/content/ai_prod_race_base_infomation_v1_1.csv')
race_infomatio_df = pd.read_csv('/content/race_base_infomation_v1_1.csv')

"""データフレイムを整えてソート"""

odds_df = odds_df.reindex(sorted(odds_df.columns), axis=1)
ai_prod_df.columns = ai_prod_df.columns.str.replace('組番_', '')
ai_prod_df = ai_prod_df.reindex(sorted(ai_prod_df.columns), axis=1)

"""AIの予測に対して予測ロジックに沿って、購入金額をbuy_listの中に入れていく。

buy_listの初期値は[0,0,0,...,0]

もし[100,0,0,...,0]であった場合'1-2'を100円買うことに相当する

買う舟券とlistの順番の対応表はres_dict参照
"""

buy_list_box =[]
for df1, df2, df3 in zip(odds_df.iterrows(), ai_prod_df.iterrows(), race_infomatio_df.iterrows()):
    index1, row1 = df1
    index2, row2 = df2
    index3, row3 = df3
    buy_list=[0] * 30

    for index, (odds, ai_pred) in enumerate(zip(row1, row2)):
      try:
        """
        ここに具体的な購入ロジック(舟券の種類ごとにいくら買うか記載)
        買う舟券とlistの順番の対応表はres_dict参照
        例では、オッズとAIの予測確率をかけて、1以上であればif分の中に入り、
        buy_listの中の指定の番号の中に購入金額を入れる
        ex.
        thred_hold = 1
        expected_val = float(odds) * float(ai_pred)
        if thred_hold <= expected_val:
          buy_list[index] = 100
        """
        thred_hold = 1
        expected_val = float(odds) * float(ai_pred)
        if thred_hold <= expected_val:
          buy_list[index] = 100
      except:
        pass
    buy_list_box.append(buy_list)

res_buy = 0
res_back = 0
res = 0
for df2, df3, buy in zip(odds_df.iterrows(), race_infomatio_df.iterrows(), buy_list_box):
    index3, row3 = df3
    index2, row2 = df2
    res_index = res_dict[row3[9]]
    pay_back = buy[res_index]/100 * row3[10]
    total_buy = sum(buy)
    res_buy = res_buy + sum(buy)
    res_back = res_back + pay_back
    this_race_res = pay_back - total_buy
    print(f"このレースで{this_race_res}円動きました")
    res = res + (pay_back - total_buy)

"""結果発表、もしresが0を超えていた場合回収率は100%を超える"""

print(f"合計購入金額は{int(res_buy)}円です。")
print(f"合計払い戻し金額は{int(res_back)}円です。")
print(f"回収率は{int(float(res_back/res_buy)*100)}%です。")
print(f"結果的に{int(res)}円です。")

