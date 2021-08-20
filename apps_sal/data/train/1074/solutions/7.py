t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        d = a.count(i)
        for j in range(1, d):
            a.remove(i)
        if d >= 2:
            c += d // 2
    print(c // 2)
    t -= 1
