s = input()
n = len(s)
if s[-1] == "1":
    print((-1))
    return

if s[0] == "0":
    print((-1))
    return

data = []
for i in range(0, n - 1):
    if s[i] == "1":
        data.append(i + 1)
        if s[n - 2 - i] == "0":
            print((-1))
            return
m = len(data)
edge = []
for i in range(1, m):
    edge.append((i, i + 1))
index = m + 1
for i in range(1, m):
    if i != 1:
        size = data[-i]
        nextsize = data[-i - 1]
        E = size - 1 - nextsize
        count = 0
        while E > count:
            edge.append((i, index))
            index += 1
            count += 1
    else:
        size = n
        nextsize = data[-2]
        E = size - 1 - nextsize
        count = 0
        while E > count:
            edge.append((i, index))
            index += 1
            count += 1

for i in range(n - 1):
    u, v = edge[i]
    print((u, v))
