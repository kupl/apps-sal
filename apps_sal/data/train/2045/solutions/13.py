import sys


class SegmTree:

    def __init__(self, array=None, size=None):
        if array is not None:
            size = len(array)
        N = 1
        while N < size:
            N <<= 1
        self.N = N
        self.tree = [0] * (2 * self.N)
        if array is not None:
            for i in range(size):
                self.tree[i + self.N] = array[i]
            self.build()

    def build(self):
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def add(self, i, value=1):
        i += self.N
        while i > 0:
            self.tree[i] += value
            i >>= 1

    def find_nonzeros(self, l, r):
        N = self.N
        l += N
        r += N
        cand = []
        while l < r:
            if l & 1:
                if self.tree[l]:
                    cand.append(l)
                l += 1
            if r & 1:
                r -= 1
                if self.tree[r]:
                    cand.append(r)
            l >>= 1
            r >>= 1
        ans = []
        while cand:
            i = cand.pop()
            if i < N:
                i <<= 1
                if self.tree[i]:
                    cand.append(i)
                if self.tree[i | 1]:
                    cand.append(i | 1)
            else:
                ans.append(i - N)
        return ans


reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
(n, m) = list(map(int, input().split()))
st = SegmTree([1] * n)
ans = [0] * n
for _ in range(m):
    (l, r, x) = list(map(int, input().split()))
    l -= 1
    x -= 1
    for i in st.find_nonzeros(l, r):
        if i != x:
            ans[i] = x + 1
            st.add(i, -1)
print(*ans)
