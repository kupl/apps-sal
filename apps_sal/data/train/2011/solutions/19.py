n = int(input())
x = 0
L = []
if n > 100:
    for i in range(n - 81, n):
        s = i % 10
        for j in range(1, 10):
            s += i // 10 ** j % 10
        if i + s == n:
            x += 1
            L.append(i)
elif n < 101:
    for i in range(1, n):
        s = i % 10 + i // 10
        if i + s == n:
            x += 1
            L.append(i)
if L == []:
    print(0)
else:
    print(x)
    for i in L:
        print(i)
