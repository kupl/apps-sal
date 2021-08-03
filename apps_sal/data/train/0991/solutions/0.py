n, k, q = list(map(int, input().split()))
mod = 10 ** 9 + 7
A = [0] * n
a, b, c, d, e, f, r, s, t, m, x = list(map(int, input().split()))
A[0] = x

for x in range(1, n):
    if pow(t, x + 1, s) <= r:
        A[x] = (a * pow(A[x - 1], 2, m) + b * A[x - 1] + c) % m
    else:
        A[x] = (d * pow(A[x - 1], 2, m) + e * A[x - 1] + f) % m


def SRMQ(arr, k):
    from collections import deque
    n = len(arr)
    ans = [None] * n
    deque = deque()
    for i in range(len(arr)):
        while deque and deque[-1] > arr[i]:
            deque.pop()
        deque.append(arr[i])
        if i >= k and arr[i - k] == deque[0]:
            deque.popleft()
        if i >= k - 1:
            ans[i - k + 1] = deque[0]
    return ans


v = SRMQ(A, k)

L1, La, Lc, Lm, D1, Da, Dc, Dm = list(map(int, input().split()))
s = 0
prod = 1
for _ in range(q):
    L1 = (La * L1 + Lc) % Lm
    D1 = (Da * D1 + Dc) % Dm
    L = L1 + 1
    R = min(L + k - 1 + D1, n)
    z = min(v[L - 1], v[R - k])
    s += z

    prod = (prod * z) % mod
print(s, prod)
