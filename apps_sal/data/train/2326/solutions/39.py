from bisect import bisect_right, bisect_left
def inpl(): return list(map(int, input().split()))


N = int(input())
A = inpl()
x = [-1]
y = [0]
for i in range(N):
    if A[i] > y[-1]:
        x.append(i)
        y.append(A[i])
ans = [0] * N
L = len(x)
k = [0] * (L + 1)
i = N - 1
base = y[-1]
for n in range(L - 1, 0, -1):
    roof = base
    base = y[n - 1]
    height = roof - base
    k[n] += k[n + 1]
    ans[x[n]] += k[n] * height
    while i >= x[n]:
        p = bisect_left(y, A[i])
        ans[x[p]] += A[i] - y[p - 1]
        k[p - 1] += 1
        i -= 1
for i in range(N):
    print((ans[i]))
