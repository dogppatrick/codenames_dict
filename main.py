import numpy as np
import pandas as pd

def escape_word(word):
    last_name = set("""陳林黃張李王吳劉蔡楊許鄭謝郭洪曾
                       邱廖賴周徐蘇葉莊呂江何蕭羅高簡朱
                       鍾施游詹沈彭胡余盧潘顏梁趙柯翁魏
                       方孫張簡戴范歐陽宋鄧杜侯曹薛傅丁
                       溫紀范姜蔣歐藍連唐馬董石卓程姚康
                       馮古姜湯汪白田涂鄒巫尤鐘龔嚴韓黎
                       阮袁童陸金錢邵任阿""")
    if word[0] in last_name or len(word)==1:
            return True
    for w in '一二三四五六七八九十年QWERTYUIOPASDFGHJKLZXCVBNM大小妳我他她鄉鎮市黨區':
        if w in word:
            return True


df = pd.read_csv("./jieba/dict.txt", sep=" ",encoding='utf-8', names=['word', 'freq', 'w_type'])
arr = np.array(df)
result = []

for data in arr:
    word, freq, w_type = data
    if freq < 250:
        continue
    if escape_word(word):
        continue
    if w_type in ['N','Vi']:
        result.append(data)

# 詞性種類
# print(set(arr[:,2]))

print(len(arr), len(result))
result.sort(key=lambda x:(x[1], x[2]))
result = np.array(result)

df_f = pd.DataFrame(result, columns=['word', 'freq', 'w_type'])
df_f.to_csv("dict_test.csv",encoding="utf-8", index=False)

# df_f = pd.DataFrame(result)
df_f['word'].to_csv(f"sample_{len(result)}.txt",encoding="utf-8", index=False, header=False)