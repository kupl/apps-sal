class SegmentTree:
    """
    0-indexed
    query : [L, R)
    """

    def __init__(self, size, initValue):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [initValue] * (2 * self.size - 1)
        self.initValue = initValue

    def cmpFunc(self, left, right):
        return left | right

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in range(self.size - 1)[:: -1]:
            self.data[i] = self.cmpFunc(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = self.cmpFunc(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = self.initValue
        while L < R:
            if R & 1:
                R -= 1
                ret = self.cmpFunc(ret, self.data[R - 1])
            if L & 1:
                ret = self.cmpFunc(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret


def cToI(s):
    return ord(s) - ord('a')


N = int(input())
S = list(map(cToI, input()))

S = [1 << s for s in S]
tree = SegmentTree(N, 0)
tree.build(S)

Q = int(input())
ans = []
for _ in range(Q):
    q1, q2, q3 = input().split()

    if q1 == '1':
        tree.update(int(q2) - 1, 1 << cToI(q3))
    else:
        ans.append(tree.query(int(q2) - 1, int(q3)))

for a in ans:
    cnt = 0
    while a > 0:
        cnt += a % 2
        a //= 2
    print(cnt)
