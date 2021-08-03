n = int(input())
P = list(map(int, input().split()))

P[:] = [x - 1 for x in P]

lst = [0] * n

i = 0
S = n - 1
ans = [1] * (n + 1)

while i < n:
    lst[P[i]] = 1
    if P[i] == S:
        k = 0
        while k == 0:
            S += -1
            if lst[S] == 0 or S == -1:
                k = 1
    i += 1
    ans[i] = i - n + S + 2

print(' '.join(map(str, ans)))
