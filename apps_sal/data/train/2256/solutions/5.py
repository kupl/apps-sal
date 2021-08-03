import sys
N, M = map(int, input().split())

Ans = [(0, 0) for _ in range(N * M)]
for i in range(1, N * M + 1):
    if i % 2:
        a, b = divmod(i // 2, M)
    else:
        a, b = divmod(N * M - i // 2, M)
    Ans[i - 1] = (a + 1, b + 1)
for a in Ans:
    sys.stdout.write('{} {}\n'.format(*a))
