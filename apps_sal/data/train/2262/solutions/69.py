def main():
    from bisect import bisect_left as bl

    class BIT():
        def __init__(self, member):
            self.member_list = sorted(member)
            self.member_dict = {v: i + 1 for i, v in enumerate(self.member_list)}
            self.n = len(member)
            self.maxmember = self.member_list[-1]
            self.minmember = self.member_list[0]
            self.maxbit = 2**(len(bin(self.n)) - 3)
            self.bit = [0] * (self.n + 1)
            self.allsum = 0

        def add(self, i, v):
            x = self.member_dict[i]
            self.allsum += v
            while x < self.n + 1:
                self.bit[x] += v
                x += x & (-x)

        def sum(self, i):
            ret = 0
            x = i
            while x > 0:
                ret += self.bit[x]
                x -= x & (-x)
            return ret

        def sum_range(self, i, j):
            return self.sum(j) - self.sum(i)

        def lowerbound(self, w):
            if w <= 0:
                return 0
            x, k = 0, self.maxbit
            while k:
                if x + k <= self.n and self.bit[x + k] < w:
                    w -= self.bit[x + k]
                    x += k
                k //= 2
            return x

        def greater(self, v):
            if v > self.maxmember:
                return None
            p = self.sum(bl(self.member_list, v))
            if p == self.allsum:
                return None
            return self.member_list[self.lowerbound(p + 1)]

        def smaller(self, v):
            if v < self.minmember:
                return None
            b = bl(self.member_list, v)
            if b == self.n:
                b -= 1
            elif self.member_list[b] != v:
                b -= 1
            p = self.sum(b + 1)
            if p == 0:
                return None
            return self.member_list[self.lowerbound(p)]

    r, c, n = list(map(int, input().split()))
    xyzw = [list(map(int, input().split())) for _ in [0] * n]
    outer = []
    for x, y, z, w in xyzw:
        if x in [0, r] or y in [0, c]:
            if z in [0, r] or w in [0, c]:
                if y == 0:
                    p = x
                elif x == r:
                    p = r + y
                elif y == c:
                    p = 2 * r + c - x
                else:
                    p = 2 * r + 2 * c - y
                if w == 0:
                    q = z
                elif z == r:
                    q = r + w
                elif w == c:
                    q = 2 * r + c - z
                else:
                    q = 2 * r + 2 * c - w
                if p > q:
                    p, q = q, p
                outer.append((p, q))

    member = [i for i, j in outer] + [j for i, j in outer] + [-1] + [2 * r + 2 * c + 1]
    bit = BIT(member)
    bit.add(-1, 1)
    bit.add(2 * r + 2 * c + 1, 1)

    outer.sort(key=lambda x: x[0] - x[1])
    for a, b in outer:
        if bit.greater(a) < b:
            print("NO")
            return
        bit.add(a, 1)
        bit.add(b, 1)
    print("YES")


main()
