import sys
input = sys.stdin.readline
Q = int(input())
D = {'R': 0, 'G': 1, 'B': 2}
for _ in range(Q):
    (N, K) = list(map(int, input().split()))
    S = input()
    mi = K
    for i in range(3):
        d = 0
        for j in range(N):
            if D[S[j]] != (i + j) % 3:
                d += 1
            if j >= K and D[S[j - K]] != (i + j - K) % 3:
                d -= 1
            if j >= K - 1:
                mi = min(mi, d)
    print(mi)
