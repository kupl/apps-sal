class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return True
        parentsA = {}

        def findA(p):
            if p not in parentsA:
                parentsA[p] = p
            if parentsA[p] != p:
                parentsA[p] = findA(parentsA[p])
            return parentsA[p]

        def unionA(p, q):
            (i, j) = (findA(p), findA(q))
            if i != j:
                parentsA[i] = j

        def isconnectedA(p, q):
            return findA(p) == findA(q)
        parentsB = {}

        def findB(p):
            if p not in parentsB:
                parentsB[p] = p
            if parentsB[p] != p:
                parentsB[p] = findB(parentsB[p])
            return parentsB[p]

        def unionB(p, q):
            (i, j) = (findB(p), findB(q))
            if i != j:
                parentsB[i] = j

        def isconnectedB(p, q):
            return findB(p) == findB(q)
        edges.sort(reverse=True)
        skip = 0
        for (typ, fr, to) in edges:
            if typ == 3:
                if isconnectedA(fr, to) and isconnectedB(fr, to):
                    skip += 1
                else:
                    unionA(fr, to)
                    unionB(fr, to)
            elif typ == 1:
                if isconnectedA(fr, to):
                    skip += 1
                else:
                    unionA(fr, to)
            elif typ == 2:
                if isconnectedB(fr, to):
                    skip += 1
                else:
                    unionB(fr, to)
        allpA = set()
        for i in range(1, n + 1):
            allpA.add(findA(i))
        allpB = set()
        for i in range(1, n + 1):
            allpB.add(findB(i))
        if len(allpA) == 1 and len(allpB) == 1:
            return skip
        return -1
