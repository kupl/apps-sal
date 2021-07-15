from collections import Counter
length = int(input())
array = list(map(int, input().split()))
dic = Counter(array)
value_list = list(dic.values())
print(len(array) - max(value_list))
