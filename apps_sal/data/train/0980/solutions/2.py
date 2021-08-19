def e_o(t):
    if t % 2 == 0:
        return 1
    else:
        return 0


def check(t):
    n = t[0]
    b = t[1]
    m = t[2]
    s = 0
    while n > 0:
        if e_o(n) == 1:
            time = n / 2 * m
            m = 2 * m
            s = s + time + b
            n = n - n / 2
        else:
            time = (n + 1) / 2 * m
            m = 2 * m
            s = s + time + b
            n = n - (n + 1) / 2
    print(s - b)


T = eval(input())
for i in range(0, T):
    t = list(map(int, input().strip().split()))
    check(t)
