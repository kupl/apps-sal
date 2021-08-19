(N, M) = map(int, input().split())
A = tuple(map(int, input().split()))
mini = 10 ** 10
bnf = 0
cnt = 1
for i in range(N):
    mini = min(mini, A[i])
    _bnf = A[i] - mini
    if _bnf > bnf:
        bnf = _bnf
        cnt = 1
    elif _bnf == bnf:
        cnt += 1
print(cnt)
