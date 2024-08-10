# 한국어 단어의 Embedding Vector 구하기


https://www.data.go.kr/data/15122687/fileData.do

위 링크에서 데이터셋을 다운받을 수 있습니다.

----
embedding.py: openai의 text-embedding-ada-002 모델을 사용하여 한국어 단어에 대한 embedding vector를 받아옵니다.

testSet: 약간의 단어들을 활용해서 embedding vector가 어떻게 나오는지 파악합니다.

----
전체 단어들은 /words/에서,   
해당 단어들에 대한 vector는 /dataset/ 에서 확인할 수 있습니다.