t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    c = l[2]
    x = c // a
    while 1:
        if a * x + b <= c:
            print(a * x + b)
            break
        else:
            x = x - 1
