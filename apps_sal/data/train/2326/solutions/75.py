class BIT:
    def __init__(self, n):
        self.N = n + 1
        self.bit = [0] * self.N

    def bit_sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def bit_add(self, i, n):
        i += 1
        while i < self.N:
            self.bit[i] += n
            i += i & -i


N, *A = list(map(int, open(0).read().split()))
inf = [(a, i) for i, a in enumerate(A)]
n = A[0]
ls = [0]
for i in range(1, N):
    if A[i] > n:
        n = A[i]
        ls.append(i)
B = BIT(N)
C = BIT(N)
inf.sort(reverse=True)
cnt = [0] * N
ccnt = [0] * N
for a, i in inf:
    B.bit_add(i, a)
    cnt[i] = B.bit_sum(N - 1) - B.bit_sum(i)
for a, i in inf:
    C.bit_add(i, 1)
    ccnt[i] = C.bit_sum(N - 1) - C.bit_sum(i)

ans = [0] * N
s = sum(A)
p = 0
x = 0
for i in range(len(ls) - 1, 0, -1):
    a = ls[i]
    b = ls[i - 1]
    m = cnt[b] - A[b] * ccnt[b]
    n = m - x
    ans[a] = n
    s -= n
    x += ans[a]
ans[0] = s
print(('\n'.join(map(str, ans))))
