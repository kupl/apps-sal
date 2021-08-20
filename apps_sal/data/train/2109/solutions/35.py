import math


def slv(A, B):
    (A, B) = (A, B) if A > B else (B, A)
    s = A * B
    c = math.floor(math.sqrt(A * B))
    if c * (c + 1) < s:
        return 2 * c - 1
    elif A == B:
        return 2 * c - 2
    elif c * c < s:
        return 2 * c - 2
    elif c * (c - 1) < s:
        return 2 * c - 3


Q = int(input())
for q in range(Q):
    (A, B) = map(int, input().split())
    print(slv(A, B))
