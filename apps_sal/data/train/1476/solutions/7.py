mod = 1000000007


def fact(n):
    if n <= 1:
        return 1
    else:
        i = 1
        for p in range(2, n + 1):
            i *= p
        return i


for _ in range(int(input())):
    S = input()
    N = len(S)
    dic = {}
    for i in range(N):
        p = S[i]
        if p in list(dic.keys()):
            dic[p] += 1
        else:
            dic[p] = 1
    f = fact(N)
    for t in list(dic.keys()):
        f = f // fact(dic[t])
    print(f % mod)
