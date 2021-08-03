n = int(input())
x2pts = {}
y2pts = {}
watchmen = {}
for i in range(n):
    watchman = tuple(map(int, input().split()))
    watchmen[watchman] = watchmen.get(watchman, 0) + 1
    x2pts[watchman[0]] = x2pts.get(watchman[0], 0) + 1
    y2pts[watchman[1]] = y2pts.get(watchman[1], 0) + 1
pairs = 0
for i in list(watchmen.items()):
    pairs -= i[1] * (i[1] - 1) // 2
for i in list(x2pts.items()):
    pairs += i[1] * (i[1] - 1) // 2
for i in list(y2pts.items()):
    pairs += i[1] * (i[1] - 1) // 2
print(pairs)
