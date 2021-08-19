import sys
input = sys.stdin.readline
(n, k) = list(map(int, input().split()))


class Union_Find:

    def __init__(self, num):
        self.par = [-1] * (num + 1)
        self.siz = [1] * (num + 1)

    def same_checker(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            x = self.par[x]
            return self.find(x)

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] < self.par[ry]:
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
            elif self.par[rx] > self.par[ry]:
                self.par[rx] = ry
                self.siz[ry] += self.siz[rx]
            else:
                self.par[rx] -= 1
                self.par[ry] = rx
                self.siz[rx] += self.siz[ry]
        return

    def size(self, x):
        return self.siz[self.find(x)]


ans = 0
guest = Union_Find(n)
for i in range(k):
    (a, b) = list(map(int, input().split()))
    if guest.same_checker(a, b):
        ans += 1
    else:
        guest.union(a, b)
print(ans)
