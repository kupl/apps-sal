import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

class Binary_Indexed_Tree():
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get(self, i):
        return self.sum_range(i, i)

    def sum(self, i):
        ret = 0
        while i:
            ret += self.data[i]
            i &= i-1
        return ret

    def sum_range(self, l, r):
        return self.sum(r)-self.sum(l-1)

    def lower_bound(self, w):
        if w<=0:
            return 0
        i = 0
        k = 1<<(self.n.bit_length())
        while k:
            if i+k <= self.n and self.data[i+k] < w:
                w -= self.data[i+k]
                i += k
            k >>= 1
        return i+1

n = int(input())
a = list(map(int, input().split()))
d = {j:i for i,j in enumerate(a)}
BIT1 = Binary_Indexed_Tree(n)
BIT2 = Binary_Indexed_Tree(n)
BIT3 = Binary_Indexed_Tree(n)

tentou = 0
ans = []
for i in range(n):
    tmp = 0
    p = d[i+1]
    inv_p = n-p
    tentou += BIT1.sum(inv_p)
    BIT1.add(inv_p, 1)

    BIT2.add(p+1, 1)
    BIT3.add(p+1, p+1)
    m = i//2+1
    mean = BIT2.lower_bound(i//2+1)
    tmp = 0
    if i%2 == 0:
        tmp -= m*(m-1)
    else:
        tmp -= m*m
    tmp += tentou
    left = BIT3.sum_range(1, mean)
    right = BIT3.sum_range(mean, n)
    if i%2 == 0:
        left = mean*m - left
        right = right - mean*m
    else:
        left = mean*m - left
        right = right - mean*(m+1)
    tmp += left + right
    ans.append(tmp)
print(*ans)


