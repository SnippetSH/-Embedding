from CalModule import normalize_l2
import os
import json

with open(os.path.join("dataset", "Embedding_with_Label.json"), "r", encoding='utf-8') as f:
    datas = json.load(f)

for key, value in datas.items():
    tmp = normalize_l2(value).tolist()

    datas[key] = tmp

#print(normed_data[0])

with open(os.path.join("dataset", "vectors_with_Label.json"), "w", encoding='utf-8') as f:
    json.dump(datas, f, ensure_ascii=False)
