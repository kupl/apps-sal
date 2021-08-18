'''
Created on Apr 30, 2016
Gmail : r.haque.249.rh@gmail.com
@author: Md. Rezwanul Haque
'''
n = int(input())
x2 = {}
y2 = {}
watchMen = {}
for i in range(n):
    watchman = tuple(map(int, input().split()))
    watchMen[watchman] = watchMen.get(watchman, 0) + 1
    x2[watchman[0]] = x2.get(watchman[0], 0) + 1
    y2[watchman[1]] = y2.get(watchman[1], 0) + 1
pairs = 0
for i in watchMen.items():
    pairs -= i[1] * (i[1] - 1) // 2
for i in x2.items():
    pairs += i[1] * (i[1] - 1) // 2
for i in y2.items():
    pairs += i[1] * (i[1] - 1) // 2
print(pairs)
