from sys import stdin
from collections import defaultdict


def input():
    return stdin.readline().strip()


for _ in range(int(input())):
    a = input()
    b = input()
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    for i in a:
        dict1[i] += 1
    for i in b:
        dict2[i] += 1
    sum1 = 0
    for i in dict1:
        min1 = min([dict1[i], dict2[i]])
        sum1 = sum1 + min1
    print(sum1)
