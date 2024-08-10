import pandas as pd
import re
import json

datas = pd.read_csv('word1.csv')
wordList = []

for data in datas["한국어 대응 표현"]:
    tmp = re.split('[^a-zA-Z0-9가-힣]', data)
    tmp = [word for word in tmp if word]
    for i in tmp:
        wordList.append(i)

print(len(wordList))

with open("words_new.json", "w", encoding='utf-8') as f:
    json.dump(wordList, f, ensure_ascii=False)

#print(datas["한국어 대응표현"])