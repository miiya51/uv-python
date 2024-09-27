import time
from random import randint

a = list()
for _ in range(100000):
    a.append(randint(1, 10000000))  # 1 ~ 10000000 の間の数値をランダムに 100000 個リストに append

for _ in range(10):  # 今回は実験のため、10回実行
    result = 0
    start_time = time.time()
    for _ in range(100000):
        num = randint(1, 10000000) # 改めて1 ~ 10000000 の間の数値をランダムに 100000 個選び、リスト中にあれば result を + 1 する
        if num in a:  # 要素がリスト中に存在するかチェック
            result += 1
    # print(result)
    print("elapsed_time_list:{time} sec".format(time=time.time() - start_time))

b = set()
for _ in range(100000):
    b.add(randint(1, 10000000))  # 1 ~ 10000000 の間の数値をランダムに 100000 個を集合に add

for _ in range(10):  # 今回は実験のため、10回実行
    result = 0
    start_time = time.time()
    for _ in range(100000):
        num = randint(1, 10000000)  # 改めて1 ~ 10000000 の間の数値をランダムに 100000 個選び、集合中にあれば result を + 1 する
        if num in b:  # 要素が集合中に存在するかチェック
            result += 1
    # print(result)
    print("elapsed_time_set:{time} sec".format(time=time.time() - start_time))