from bisect import *


def sub_string(temp, n, l, r):
    index = bisect_left(temp, l - 1)
    if index >= n:
        print('NO')
        return
    if temp[index] + 2 <= r - 1:
        print('YES')
    else:
        print('NO')


for _ in range(int(input())):
    (n, q) = map(int, input().split())
    s = [x for x in input()]
    temp = []
    for i in range(n - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            temp.append(i)
    n = len(temp)
    for i in range(q):
        (l, r) = map(int, input().split())
        sub_string(temp, n, l, r)
