from operator import add
import sys
input = sys.stdin.readline


class SegTree():
    def __init__(self, N, e, operator_func=add):
        self.e = e  # 単位元
        self.size = N
        self.node = [self.e] * (2 * N)
        self.operator_func = operator_func  # 処理(add or xor max minなど)

    def set_list(self, l):
        for i in range(self.size):
            self.node[i + self.size - 1] = l[i]
        for i in range(self.size - 1)[::-1]:
            self.node[i] = self.operator_func(self.node[2 * i + 1], self.node[2 * i + 2])

    def update(self, k, x):
        k += self.size - 1
        self.node[k] = x
        while k >= 0:
            k = (k - 1) // 2
            self.node[k] = self.operator_func(self.node[2 * k + 1], self.node[2 * k + 2])

    def get(self, l, r):
        # [l, r) についてqueryを求める
        x = self.e
        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                x = self.operator_func(x, self.node[l - 1])
                l += 1
            if r & 1:
                r -= 1
                x = self.operator_func(x, self.node[r - 1])
            l >>= 1
            r >>= 1
        return x


def main():
    S = input()
    T = input()
    treeS = SegTree(len(S), 0)
    treeT = SegTree(len(T), 0)
    treeS.set_list([1 if s == "A" else 0 for s in S])
    treeT.set_list([1 if s == "A" else 0 for s in T])

    q = int(input())
    for _ in range(q):
        a, b, c, d = list(map(int, input().split()))
        sa = treeS.get(a - 1, b)
        sb = b - a + 1 - sa
        ta = treeT.get(c - 1, d)
        tb = d - c + 1 - ta

        if (2 * (sb - sa) + tb - ta) % 3 or (sb - sa + 2 * (tb - ta)) % 3:
            print("NO")
        else:
            print("YES")


main()
