from CalModule import normalize_l2
import os
import json

with open(os.path.join("dataset", "Embedding_new.json"), "r") as f:
    datas = json.load(f)

normed_data = []
for data in datas:
    normed_data.append(normalize_l2(data).tolist())

#print(normed_data[0])

with open(os.path.join("dataset", "vector1.json"), "w") as f:
    json.dump(normed_data, f)
