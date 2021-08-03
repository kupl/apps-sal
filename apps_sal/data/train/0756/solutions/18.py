for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    c = x + y
    n = 1
    while(True):
        t = c + n
        for i in range(2, t):
            if t % i == 0:
                break
        else:
            break
        n += 1
    print(n)
