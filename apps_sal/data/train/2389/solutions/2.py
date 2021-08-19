import sys
input = sys.stdin.readline
q = int(input())
for testcases in range(q):
    (n, k) = list(map(int, input().split()))
    S = list(input().strip())
    for i in range(n):
        if S[i] == 'R':
            S[i] = 0
        elif S[i] == 'G':
            S[i] = 1
        else:
            S[i] = 2
    ANS = 1 << 50
    for mod in range(3):
        SUM = 0
        for i in range(k):
            if S[i] % 3 != (mod + i) % 3:
                SUM += 1
        ANS = min(ANS, SUM)
        for i in range(k, n):
            if S[i - k] != (mod + (i - k)) % 3:
                SUM -= 1
            if S[i] != (mod + i) % 3:
                SUM += 1
            ANS = min(ANS, SUM)
    print(ANS)
