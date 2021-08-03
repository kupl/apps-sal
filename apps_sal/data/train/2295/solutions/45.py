
N = int(input())
res = float("inf")
S = 0
cnt = 0
for _ in range(N):
    A, B = map(int, input().split())
    S += A
    if A > B:
        res = min(B, res)
    if A == B:
        cnt += 1
print(S - res if cnt != N else 0)
