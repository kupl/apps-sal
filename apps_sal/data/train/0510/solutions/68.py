class SegTree:
    def __init__(self, N, S):
        self.N = 2 ** ((N - 1).bit_length())
        self.tree = [0 for i in range(self.N * 2 - 1)]
        for i in range(len(S)):
            self.tree[self.N - 1 + i] = 1 << (ord(S[i]) - ord("a"))

        for i in range(self.N - 2, -1, -1):
            self.tree[i] = self.tree[i * 2 + 1] | self.tree[i * 2 + 2]

    def update(self, index, char):
        i = self.N - 1 + index
        # アルファベットがある = bitが立っている
        self.tree[i] = 1 << (ord(char) - ord("a"))
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = self.tree[i * 2 + 1] | self.tree[i * 2 + 2]

    def get(self, a, b):
        return self.query(a, b, 0, 0, self.N)

    # k : ノードの番号
    # l : ノードkの受け持つ区間
    # r : ノードkの受け持つ区間
    def query(self, a, b, k, l, r):
        if r <= a or b <= l:  # 区間外
            return 0
        elif a <= l and r <= b:  # 受け持ち区間は完全に含まれている
            return self.tree[k]
        else:  # 一部含まれてる
            left = self.query(a, b, 2 * k + 1, l, (l + r) // 2)
            right = self.query(a, b, 2 * k + 2, (l + r) // 2, r)
            return left | right


def solve():
    N = int(input())
    S = list(input().strip())
    tree = SegTree(N, S)

    Q = int(input())
    for _ in range(Q):
        t_q, in_1, in_2 = input().split()
        if t_q == "1":
            i_q = int(in_1)
            c_q = in_2
            tree.update(i_q - 1, c_q)
        else:
            l_q = int(in_1)
            r_q = int(in_2)
            print(bin(tree.get(l_q - 1, r_q)).count("1"))


solve()
