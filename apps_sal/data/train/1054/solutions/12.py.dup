for _ in range(int(input())):
    S = list(input())
    N = len(S)
    c = True
    for i in range(N):
        if S[i] != '.' and S[i] != S[N - i - 1] and S[N - i - 1] != '.':
            c = False
            print('-1')
            break
        elif S[i] == '.' and S[N - i - 1] == '.':
            S[i] = S[N - i - 1] = 'a'
        elif S[i] == '.' and S[N - i - 1] != '.':
            S[i] = S[N - i - 1]
    if c:
        p = ''
        for i in S:
            p += i
        print(p)
