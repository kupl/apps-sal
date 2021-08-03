from sys import stdin


class UnionFind:
    def __init__(self, n):
        self.tree = [-1 for i in range(n)]
        return

    def union(self, x, y):
        xroot = self.root(x)
        yroot = self.root(y)
        if xroot == yroot:
            return
        if self.tree[xroot] > self.tree[yroot]:
            xroot, yroot = yroot, xroot
        self.tree[xroot] += self.tree[yroot]
        self.tree[yroot] = xroot
        return

    def root(self, x):
        qu = []
        while self.tree[x] >= 0:
            qu.append(x)
            x = self.tree[x]
        for i in qu:
            self.tree[i] = x
        return x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self):
        arr = [0 for i in range(len(self.tree))]
        for i in range(len(self.tree)):
            arr[self.root(i)] += 1
        for i in range(len(self.tree)):
            if self.root(i) != i:
                arr[i] += arr[self.root(i)]
        return arr

    def getnumroots(self):
        ans = 0
        for i in self.tree:
            if i < 0:
                ans += 1
        return ans

    def getelements(self):
        arr = [-1 for i in range(len(self.tree))]
        ans = []
        c = 0
        for i in range(len(self.tree)):
            if arr[self.root(i)] == -1:
                arr[self.root(i)] = c
                ans.append([i])
                c += 1
            else:
                ans[arr[self.root(i)]].append(i)
        return ans


def input():
    return stdin.readline()


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    uf = UnionFind(n)
    ans = 0
    for i in range(m):
        x, y = map(int, input().split())
        uf.union(x - 1, y - 1)
    arr = uf.getelements()
    for i in range(len(arr)):
        temp = []
        for j in arr[i]:
            temp.append(p[j] - 1)
        ans += len(set(temp).intersection(arr[i]))
    print(ans)


def __starting_point():
    main()


__starting_point()
