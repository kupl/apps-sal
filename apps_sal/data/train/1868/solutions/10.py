class Solution:

    def beautifulArray(self, N: int) -> List[int]:
        self.N = N
        self.rst = []
        counter = 0
        while N > 0:
            N = N >> 1
            counter += 1
        self.tree = [0] * 2 ** (counter + 1)
        self.tree[0] = 1
        self.buildtree(0, 0)
        self.traverse(0)
        return self.rst

    def traverse(self, i):
        if 2 * i + 1 > len(self.tree) or self.tree[2 * i + 1] == 0:
            self.rst.append(self.tree[i])
        else:
            self.traverse(2 * i + 1)
            self.traverse(2 * i + 2)

    def buildtree(self, i, level):
        if self.tree[i] + 2 ** level <= self.N:
            self.tree[2 * i + 1] = self.tree[i]
            self.tree[2 * i + 2] = self.tree[i] + 2 ** level
            self.buildtree(2 * i + 1, level + 1)
            self.buildtree(2 * i + 2, level + 1)
