for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    s = x + y
    n = 1
    while(True):
        t = s + n
        for i in range(2, t):
            if t % i == 0:
                break
        else:
            break
        n += 1
    print(n)
