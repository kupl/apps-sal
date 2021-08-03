# cook your dish here
from collections import Counter
for i in range(int(input())):
    n = int(input())
    s = input()
    res = Counter(s)

    re = abs(res['D'] - res['U']) + abs(res['L'] - res['R'])
    print(n - re)
