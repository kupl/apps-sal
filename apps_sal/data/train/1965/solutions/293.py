class Solution:
    def find(self, root: List[int], x: int):
        if x != root[x]:
            root[x] = self.find(root, root[x])
        return root[x]

    def uni(self, root: List[int], x: int, y: int) -> bool:
        x, y = self.find(root, x), self.find(root, y)
        if x == y:
            return False
        root[x] = y
        return True

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        l = len(edges)
        root = list(range(0, n + 1))
        for ed in edges:
            if ed[0] == 3:
                self.uni(root, ed[1], ed[2])

        for i in range(1, n + 1):
            self.find(root, i)

        sero = set(root)
        np = len(sero) - 1

        ret = l - (n + np - 2)
        if ret < 0:
            return -1

        root1 = root.copy()
        root2 = root.copy()
        for ed in edges:
            if ed[0] == 1:
                self.uni(root1, ed[1], ed[2])
            if ed[0] == 2:
                self.uni(root2, ed[1], ed[2])

        for i in range(1, n + 1):
            self.find(root1, i)
            self.find(root2, i)

        if len(set(root1)) == 2 and len(set(root2)) == 2:
            return ret
        else:
            return -1

        ret = l - (size - ll + 2 * (n - size + ll - 1))
        if ret < 0:
            return -1
        else:
            return ret

        l = len(edges)
        conn = [0 for x in range(0, n)]
        nn = [0 for x in range(0, n)]
        cnt = 2
        for ed in edges:
            if ed[0] == 3:
                nn[ed[1]] = nn[ed[2]] = 2
