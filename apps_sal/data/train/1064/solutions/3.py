def isPossible(l):
    if (l[0] == 'C' or l[0] == '?') and (l[1] == 'H' or l[1] == '?') and (l[2] == 'E' or l[2] == '?') and (l[3] == 'F' or l[3] == '?'):
        return True
    else:
        return False


T = int(input())
ans = []
for _ in range(T):
    S = list(input())
    N = len(S)
    for i in range(N - 1, 2, -1):
        if isPossible(S[i - 3:i + 1]):
            S[i] = 'F'
            S[i - 1] = 'E'
            S[i - 2] = 'H'
            S[i - 3] = 'C'
    for i in range(N):
        if S[i] == '?':
            S[i] = 'A'
    s = ''
    for i in S:
        s += i
    ans.append(s)
for i in ans:
    print(i)
