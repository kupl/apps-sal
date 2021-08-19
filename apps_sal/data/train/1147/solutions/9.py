# cook your dish here
from collections import defaultdict


def my_fun():
    return 0


t = int(input())
for _ in range(t):
    count = 0
    n = int(input())
    s = input()
    hm = dict()
    for i in range(n):
        hm[s[i]] = hm.get(s[i], 0) + 1
    if n % 2 != 0:
        flag = 0
        for key, value in list(hm.items()):
            if value % 2 != 0 and flag != 1:
                flag = 1
            elif value % 2 != 0 and flag == 1:
                count += 1
    else:
        for key, value in list(hm.items()):
            if value % 2 != 0:
                count += 1
        if count != 0:
            count -= 1

    print(count)
