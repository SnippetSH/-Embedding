import json
from CalModule import cos_sim, normalize_l2
import os

norm_vectors = []
for i in range(11):
    with open(os.path.join("testSet", f"embedding_{i}.json"), "r") as f:
        v = json.load(f)
    norm_vectors.append(normalize_l2(v))
print(norm_vectors)

print(f"사과 and 포도: {cos_sim(norm_vectors[0], norm_vectors[1])}")
print(f"사과 and 바나나: {cos_sim(norm_vectors[0], norm_vectors[2])}")
print(f"사과 and 죄송해요: {cos_sim(norm_vectors[0], norm_vectors[3])}")
print(f"사과 and 감사합니다: {cos_sim(norm_vectors[0], norm_vectors[4])}")
print(f"사과 and 잠: {cos_sim(norm_vectors[0], norm_vectors[5])}")
print(f"사과 and 기차: {cos_sim(norm_vectors[0], norm_vectors[6])}")
print(f"사과 and 선생님: {cos_sim(norm_vectors[0], norm_vectors[7])}")
print(f"사과 and 버스: {cos_sim(norm_vectors[0], norm_vectors[8])}")
print(f"사과 and 과학: {cos_sim(norm_vectors[0], norm_vectors[9])}")
print(f"사과 and 과일: {cos_sim(norm_vectors[0], norm_vectors[10])}")