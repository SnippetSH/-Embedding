from openai import OpenAI
import json
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key="YOUR_OPENAI_API_KEY"
)

#input_data = ["사과", "포도", "바나나", "죄송해요", "감사합니다", "잠", "기차", "선생님", "버스", "과학", "과일"]

with open(os.path.join("words", "words.json"), "r", encoding='utf-8') as f:
    input_data1 = json.load(f)

with open(os.path.join("words", "words_new.json"), "r", encoding='utf-8') as f:
    input_data2 = json.load(f)

input_data = input_data1 + input_data2
input_data = list(set(input_data))
print(input_data[0])

# 결과를 담을 리스트
all_vectors = {}

# 입력 데이터를 나누어 처리
batch_size = 100  # 한 번에 처리할 텍스트의 개수
for i in range(0, len(input_data), batch_size):
    batch = input_data[i:i+batch_size]  # 현재 배치 생성
    
    # OpenAI API 호출
    response = client.embeddings.create(
        input=batch, 
        model="text-embedding-ada-002"
    )
    
    # 각 텍스트의 임베딩 벡터를 리스트에 추가
    for j, word in enumerate(batch):
        all_vectors[word] = response.data[j].embedding[:256]

print(all_vectors["장인"])

with open(os.path.join("dataset", "Embedding_with_Label.json"), "w", encoding='utf-8') as f:
    json.dump(all_vectors, f, ensure_ascii=False)