"""
Problem 2, Points on Line
Sizhang Zhao 1200011770
"""
from collections import deque


def number(D, d, length, tem):
    if tem < length:
        if tem == 0:
            start = 1
            num = 0
        else:
            start = tem
            num = tem - 1
        for i in range(start, length):
            if D[i] - D[0] <= d:
                num += 1
            else:
                break
    else:
        num = tem - 1
    if num < 2:
        return 0
    else:
        return num


(n, d) = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]
D = deque(numbers)
leng = len(D)
times = 0
tem = 0
while leng >= 3:
    leng = len(D)
    tem = number(D, d, leng, tem)
    times += tem * (tem - 1) / 2
    D.popleft()
print(int(times))
