import copy


def union(subsets, u, v):
    uroot = find(subsets, u)
    vroot = find(subsets, v)

    if subsets[uroot][1] > subsets[vroot][1]:
        subsets[vroot][0] = uroot
    if subsets[vroot][1] > subsets[uroot][1]:
        subsets[uroot][0] = vroot
    if subsets[uroot][1] == subsets[vroot][1]:
        subsets[vroot][0] = uroot
        subsets[uroot][1] += 1


def find(subsets, u):
    if subsets[u][0] != u:
        subsets[u][0] = find(subsets, subsets[u][0])
    return subsets[u][0]


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        subsets1 = ['1 index'] + [[x + 1, 0] for x in range(n)]
        subsets2 = ['1 index'] + [[x + 1, 0] for x in range(n)]

        e = 0
        e1 = 0
        e2 = 0
        i = 0

        while e < n - 1:
            if i == len(edges):
                i = 0
                break
            typ, u, v = edges[i]
            if typ != 3:
                i += 1
                continue
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                e += 1

            i += 1

        e1 = e
        e2 = e
        subsets2 = copy.deepcopy(subsets1)
        i = 0
        while e2 < n - 1:
            if i == len(edges):
                i = 0
                break
            typ, u, v = edges[i]
            if typ != 2:
                i += 1
                continue
            if find(subsets2, u) != find(subsets2, v):
                union(subsets2, u, v)
                e += 1
                e2 += 1
            i += 1

        if e2 < n - 1:
            return -1

        i = 0
        while e1 < n - 1:
            if i == len(edges):
                return -1

            typ, u, v = edges[i]
            if typ != 1:
                i += 1
                continue

            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                e += 1
                e1 += 1
            i += 1

        return len(edges) - e
