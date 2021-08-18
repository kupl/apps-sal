class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        parentsA = list(range(n))
        parentsB = list(range(n))

        def find(parents, a):
            while a != parents[a]:
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a

        def union(parents, a, b):
            a = find(parents, a)
            b = find(parents, b)
            parents[a] = b

        type3 = []
        typeB = []
        typeA = []

        for t, u, v in edges:
            u, v = u - 1, v - 1
            if t == 3:
                type3.append((u, v))
            elif t == 2:
                typeB.append((u, v))
            elif t == 1:
                typeA.append((u, v))

        add = 0
        for u, v in type3:
            if find(parentsA, u) != find(parentsA, v):
                add += 1
                union(parentsA, u, v)
                union(parentsB, u, v)

        for u, v in typeA:
            if find(parentsA, u) != find(parentsA, v):
                add += 1
                union(parentsA, u, v)

        for u, v in typeB:
            if find(parentsB, u) != find(parentsB, v):
                add += 1
                union(parentsB, u, v)

        uniqA, uniqB = set(), set()
        for i in range(n):
            uniqA.add(find(parentsA, i))
            uniqB.add(find(parentsB, i))

            if len(uniqA) > 1 or len(uniqB) > 1:
                return -1

        return len(edges) - add
