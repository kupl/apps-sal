class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(roots, x):
            if x == roots[x]:
                return x
            else:
                roots[x] = find(roots, roots[x])
                return roots[x]

        pairs1 = []
        pairs2 = []
        pairs3 = []

        for type, x, y in edges:
            if type == 1:
                pairs1.append((x, y))
            elif type == 2:
                pairs2.append((x, y))
            else:
                pairs3.append((x, y))

        roots = [i for i in range(n + 1)]
        rootSet = set(range(1, n + 1))
        res = 0

        for x, y in pairs3:
            root1 = find(roots, x)
            root2 = find(roots, y)

            if root1 != root2:
                roots[root2] = root1
                rootSet.remove(root2)
            else:
                res += 1

        root1Set = set(rootSet)
        root2Set = set(rootSet)
        roots1 = list(roots)
        roots2 = list(roots)

        for x, y in pairs1:
            root1 = find(roots1, x)
            root2 = find(roots1, y)

            if root1 != root2:
                roots1[root2] = root1
                root1Set.remove(root2)
            else:
                res += 1

        for x, y in pairs2:
            root1 = find(roots2, x)
            root2 = find(roots2, y)

            if root1 != root2:
                roots2[root2] = root1
                root2Set.remove(root2)
            else:
                res += 1

        if len(root1Set) != 1 or len(root2Set) != 1:
            return -1
        return res
