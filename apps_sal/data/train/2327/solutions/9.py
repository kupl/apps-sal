import sys
def input():
    return sys.stdin.readline()[:-1]

N, M = list(map(int, input().split()))
L = []
for i in range(N):
    l, r = list(map(int, input().split()))
    L.append((r - l + 1, l, r + 1))
L.sort()


class Bit:
    """
    0-indexed
    # 使用例
    bit = Bit(10)  # 要素数
    bit.add(2, 10)
    print(bit.sum(5))  # 10
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


class BitImos:
    """
    ・範囲すべての要素に加算
    ・ひとつの値を取得
    の2種類のクエリをO(logn)で処理
    """

    def __init__(self, n):
        self.bit = Bit(n + 1)

    def add(self, s, t, x):
        # [s, t)にxを加算
        self.bit.add(s, x)
        self.bit.add(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        # 位置iの値を取得
        return self.bit.sum(key + 1)


imos = BitImos(M + 1)
il = 0
a = N
for i in range(1, M + 1):
    while il < N:
        ra, l, r = L[il]
        if i < ra:
            break
        il += 1
        a -= 1
        imos.add(l, r, 1)
    ans = 0
    for j in range(i, M + 1, i):
        ans += imos[j]

    print((ans + a))

