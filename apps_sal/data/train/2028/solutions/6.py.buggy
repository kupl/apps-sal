s = input()
N = len(s)
if len(set(list(s))) == 1:
    print('Impossible')
else:
    if len(set(list(s))) == 2:
        t = list(set(list(s)))
        k1, k2 = t[0], t[1]
        if s.count(k1) == N - 1 or s.count(k2) == N - 1:
            print('Impossible')
            return

    t = s
    for i in range(N):
        t = t[1:] + t[0]
        if t != s and t[::-1] == t:
            print(1)
            return

    print(2)
