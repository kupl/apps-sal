t = int(input())
while t > 0:
    n, m = map(int, input().split())
    l = []
    co = 0
    for i in range(n):
        l.append(input())
    for i in range(m):
        c = 0
        for j in range(n):
            if l[j][i] == "1":
                c += 1
        co += c * (c - 1) / 2
    print(int(co))
    t -= 1
