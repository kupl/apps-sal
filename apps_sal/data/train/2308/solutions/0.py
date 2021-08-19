from collections import deque
import sys
input = sys.stdin.readline


def slidemax(X, k):
    q = deque([])
    ret = []
    for i in range(len(X)):
        while q and q[-1][1] <= X[i]:
            q.pop()
        deque.append(q, (i + k, X[i]))
        if q[0][0] == i:
            deque.popleft(q)
        if i >= k - 1:
            ret.append(q[0][1])
    return ret


(N, W) = list(map(int, input().split()))
A = [0] * W
s = 0
for _ in range(N):
    (l, *B) = list(map(int, input().split()))
    if l * 2 < W:
        C = slidemax([0] * (l - 1) + B + [0] * (l - 1), l)
        m = max(B + [0])
        s += m
        for i in range(l - 1):
            A[i] += C[i] - m
            A[-i - 1] += C[-i - 1] - m
    else:
        C = slidemax([0] * (W - l) + B + [0] * (W - l), W - l + 1)
        A = [a + c for (a, c) in zip(A, C)]
print(*[a + s for a in A])
