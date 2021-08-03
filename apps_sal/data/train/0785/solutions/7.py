for _ in range(int(input())):
    a = int(input())
    c = 1
    d = 1
    ans = []
    while c < (d * a):
        ans.append((d * a) - c)
        c += 2**d
        d += 1
    t_1 = ans.index(max(ans)) + 1
    print(d - 1, t_1, sep=' ')
