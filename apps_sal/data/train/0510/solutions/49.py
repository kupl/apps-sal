class SegmentTree:
    """Segmant Tree for query process.

    Args:
      a (List[int]): array.
      identity (int): identity element with f.
    """

    def __init__(self, a, identity=0):
        self.a = a
        self.n = len(a)
        self.identity = identity
        self.depth = (self.n - 1).bit_length()
        self.segment = (1 << self.depth) - 1
        self.tree = [identity] * (self.segment * 2 + 1)
        self.tree[self.segment:self.n + self.segment] = a
        for i in range(self.segment - 1, -1, -1):
            self.tree[i] = self.f(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def update(self, i: int, x: int):
        i += self.segment
        self.tree[i] = x
        while i:
            i = (i - 1) // 2
            self.tree[i] = self.f(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def query(self, l: int, r: int) -> int:
        """Query at [l, r]

        Args:
          l (int): left
          r (int): right

        Returns:
          int: result
        """
        if l > r:
            return self.identity
        l += self.segment
        r += self.segment
        res = self.identity
        while l <= r:
            if not l & 1:
                res = self.f(self.tree[l], res)
            if r & 1:
                res = self.f(res, self.tree[r])
            l = l // 2
            r = (r - 2) // 2
        return res

    def f(self, x: int, y: int) -> int:
        return x | y


n = int(input())
s = input()
q = int(input())
a = ord('a')
segment_tree = SegmentTree([1 << ord(c) - a for c in s])
for _ in range(q):
    query = input().split()
    if query[0] == '1':
        i = int(query[1]) - 1
        c = query[2]
        segment_tree.update(i, 1 << ord(c) - a)
    else:
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        bit = segment_tree.query(l, r)
        print(format(bit, 'b').count('1'))
