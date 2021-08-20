class DSU:

    def __init__(self, n):
        self.par = list(range(n))
        self.arr = list(map(int, input().split()))
        self.siz = [1] * n
        self.sht = [0] * n
        self.max = 0

    def find(self, n):
        nn = n
        while nn != self.par[nn]:
            nn = self.par[nn]
        while n != nn:
            (self.par[n], n) = (nn, self.par[n])
        return n

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.siz[a] < self.siz[b]:
            (a, b) = (b, a)
        self.par[b] = a
        self.siz[a] += self.siz[b]
        self.arr[a] += self.arr[b]
        if self.arr[a] > self.max:
            self.max = self.arr[a]

    def add_node(self, n):
        self.sht[n] = 1
        if self.arr[n] > self.max:
            self.max = self.arr[n]
        if n != len(self.par) - 1 and self.sht[n + 1]:
            self.union(n, n + 1)
        if n != 0 and self.sht[n - 1]:
            self.union(n, n - 1)


def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    dsu = DSU(n)
    per = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[~i] = dsu.max
        dsu.add_node(per[~i] - 1)
    for x in ans:
        print(x)
    return 0


main()
