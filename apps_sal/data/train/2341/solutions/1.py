import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N, M, K = list(map(int, input().split()))
    K = min(K, M - 1)
    A = [int(a) for a in input().split()]
    B = [max(A[i], A[-M + i]) for i in range(M)]
    print(max([min(B[i:i + M - K]) for i in range(K + 1)]))
