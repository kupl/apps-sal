t = int(input())
for i in range(t):
    n = int(input())
    new = []
    d = 0
    for i in range(n):
        s, j = list(map(int, input().split()))
        c = j - s
        new.append(c)
    for i in new:
        if i > 5:
            d = d + 1
    print(d)
