import sys
T = int(input())
fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
for t in range(T):
    N = sys.stdin.readline().strip()
    cnt = 0
    for n in N:
        cnt += fact[int(n)]
    if str(cnt) == N:
        print(1)
    else:
        print(0)
