class SegmentTree:
    """
    非再帰
    segment tree
    """

    def __init__(self, n, func, init=float('inf')):
        """
        n->配列の長さ
        func:func(a,b)->val,\u3000func=minだとRMQになる
        木の高さhとすると,
        n:h-1までのノード数。h段目のノードにアクセスするために使う。
        data:ノード。
        parent:k->child k*2+1とk*2+2
        """
        self.n = 2 ** (n - 1).bit_length()
        self.init = init
        self.data = [init] * (2 * self.n)
        self.func = func

    def set(self, k, v):
        """
        値の初期化
        """
        self.data[k + self.n - 1] = v

    def build(self):
        """
        setの後に一斉更新
        """
        for k in reversed(list(range(self.n - 1))):
            self.data[k] = self.func(self.data[k * 2 + 1], self.data[k * 2 + 2])

    def update(self, k, a):
        """
        list[k]=aに更新する。
        更新ぶんをrootまで更新
        """
        k += self.n - 1
        self.data[k] = a
        while k > 0:
            k = (k - 1) // 2
            self.data[k] = self.func(self.data[k * 2 + 1], self.data[k * 2 + 2])

    def query(self, l, r):
        """
        [l,r)のfuncを求める
        """
        L = l + self.n
        R = r + self.n
        ret = self.init
        while L < R:
            if R & 1:
                R -= 1
                ret = self.func(ret, self.data[R - 1])
            if L & 1:
                ret = self.func(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret


N = int(input())
S = input()
Q = int(input())
Seg = SegmentTree(N, lambda x, y: x | y, 0)


def a2n(a):
    return ord(a) - ord('a')


def createBit(a):
    return 1 << a2n(a)


for (i, s) in enumerate(S):
    Seg.set(i, createBit(s))
Seg.build()
for _ in range(Q):
    (t, l, r) = input().split()
    if int(t) == 1:
        Seg.update(int(l) - 1, createBit(r))
    else:
        print(bin(Seg.query(int(l) - 1, int(r))).count('1'))
