class DSU(object):
    def __init__(self, n):
        self.father = list(range(n))
        self.size = n

    def union(self, x, s):
        x = self.find(x)
        s = self.find(s)
        if x == s:
            return
        self.father[s] = x
        self.size -= 1

    def find(self, x):
        xf = self.father[x]
        if xf != x:
            self.father[x] = self.find(xf)
        return self.father[x]


def is_invalid(a, b, ds):
    return ds.find(a) == ds.find(b)


n, k = list(map(int, input().split()))
ds = DSU(n * 2)
for i in range(k):
    first, second, color = list(map(int, input().split()))
    first -= 1
    second -= 1
    if color == 0:
        if is_invalid(first, second, ds):
            print(0)
            return
        ds.union(first, second + n)
        ds.union(first + n, second)
    else:
        if is_invalid(first, second + n, ds):
            print(0)
            return
        ds.union(first, second)
        ds.union(first + n, second + n)

sum = 1
for i in range(ds.size // 2 - 1):
    sum = (sum * 2) % (10 ** 9 + 7)
print(sum)
