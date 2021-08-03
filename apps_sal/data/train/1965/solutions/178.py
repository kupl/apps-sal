class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        edges.sort(key=lambda x: -x[0])

        father1 = [i for i in range(n + 1)]
        size1 = [1 for i in range(n + 1)]
        father2 = [i for i in range(n + 1)]
        size2 = [1 for i in range(n + 1)]

        def find(a, typ):

            if typ == 1:

                path = []

                while a != father1[a]:
                    path.append(a)
                    a = father1[a]

                for b in path:
                    father1[b] = a

                return a

            elif typ == 2:

                path = []

                while a != father2[a]:
                    path.append(a)
                    a = father2[a]

                for b in path:
                    father2[b] = a

                return a

        def union(a, b, typ):

            fa, fb = find(a, typ), find(b, typ)
            if fa == fb:
                return

            if typ == 1:

                father1[fa] = fb
                size1[fb] += size1[fa]

            else:

                father2[fa] = fb
                size2[fb] += size2[fa]

            return

        necessary = 0

        for edge in edges:
            typ, a, b = edge

            if typ == 3:

                if find(a, 1) != find(b, 1):

                    necessary += 1

                    union(a, b, 1)
                    union(a, b, 2)

            elif typ == 1:

                if find(a, 1) != find(b, 1):

                    necessary += 1

                    union(a, b, 1)

            else:

                if find(a, 2) != find(b, 2):

                    necessary += 1

                    union(a, b, 2)

        if size1[find(1, 1)] != n or size2[find(1, 2)] != n:
            return -1

        return len(edges) - necessary
