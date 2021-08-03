for _ in range(int(input())):
    S = list(input())
    N = len(S)
    c = False
    for i in range(N):
        p = S.copy()
        del p[i:i + 1]
        if p == p[::-1]:
            c = True
            break
    if c:
        print('YES')
    else:
        print('NO')
