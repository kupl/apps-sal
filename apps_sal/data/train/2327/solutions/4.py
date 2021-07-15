class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, k, x):
        while k <= self.n:
            self.bit[k] += x
            k += k & -k

    def sum(self, k):
        s = 0
        while k > 0:
            s += self.bit[k]
            k -= k & -k
        return s


n, m = list(map(int, input().split()))
st = BIT(m)
L, R = [], []
d = [[] for i in range(m + 1)]
for i in range(n):
    l, r = list(map(int, input().split()))
    L.append(l)
    R.append(r)
    d[r - l + 1].append(i)

num = n
for i in range(1, m + 1):
    num -= len(d[i])
    for j in d[i]:
        st.add(L[j], 1)
        st.add(R[j] + 1, -1)

    tmp = 0
    k = i
    for j in range(k, m + 1, i):
        tmp += st.sum(j)

    print((num + tmp))

