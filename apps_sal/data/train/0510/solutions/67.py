n = int(input())
s = list(input())

dic = {}
for i in range(26):
    dic[chr(i+97)] = []

for i in range(n):
    dic[s[i]].append(i)

for i in range(26):
    dic[chr(i+97)].append(float('inf'))

from bisect import bisect_left
q = int(input())
for i in range(q):
    x, y, z = input().split()
    if x == '1':
        y = int(y) - 1
        p = bisect_left(dic[s[y]], y)
        dic[s[y]].pop(p)
        dic[z].insert(bisect_left(dic[z], y), y)
        s[y] = z
    else:
        res = 0
        y, z = int(y) - 1, int(z) - 1
        for i in range(26):
            p = dic[chr(i+97)][bisect_left(dic[chr(i+97)], y)]
            if p <= z:
                res += 1
        print(res)
