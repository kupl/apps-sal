t = int(input())
while t > 0:
    n = int(input())
    l = [list(map(int, input().split())) for i in range(n)]
    c = 0
    for i in l:
        c += i.count(0)
    c = c // 2
    i = 1
    while c >= 0:
        c -= i
        i += 1
    print(n - i + 1)
    t -= 1
