from collections import Counter
from copy import copy
import random


def derange(arr, max_freq):
    new_arr = copy(arr)
    dis = []
    for (index, item) in enumerate(new_arr):
        dis.append((item, index))
    dis.sort()
    (item, index) = ([a for (a, b) in dis], [b for (a, b) in dis])
    item = item[-max_freq:] + item[:-max_freq]
    dis = list(zip(item, index))
    new_arr = [0] * len(new_arr)
    for (a, b) in dis:
        new_arr[b] = a
    return new_arr


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = Counter(arr)
    flag = 1
    val = list(freq.values())
    for i in val:
        if 2 * i > n:
            flag = 0
    if flag != 0:
        print('Yes')
        new = derange(arr, max(val))
        print(*new)
    else:
        print('No')
