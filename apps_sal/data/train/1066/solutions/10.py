def check(n):
    l = list(map(int, str(n)))
    t = len(l)
    p = t - 1
    for i in range(t - 1, 0, -1):
        if l[i] < l[i - 1]:
            l[i - 1] -= 1
            p = i - 1

    for i in range(p + 1, t):
        l[i] = 9
    return int(''.join(map(str, l)))


try:
    for _ in range(int(input())):
        n = int(input())
        print(check(n))
except EOFError as e:
    pass
