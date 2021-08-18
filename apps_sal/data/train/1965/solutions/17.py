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

        mst1 = set()
        mst2 = set()
        subsets1 = ['1 index'] + [[x + 1, 0] for x in range(n)]
        subsets2 = ['1 index'] + [[x + 1, 0] for x in range(n)]

        edges = sorted(edges, key=lambda e: -e[0])
        e = 0
        e1 = 0
        e2 = 0
        i = 0

        while e < n - 1:
            if i == len(edges):
                return -1
            typ, u, v = edges[i]
            if typ != 3:
                break
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)
                mst1.add(u)
                mst1.add(v)
                e += 1

            i += 1

        e1 = e
        e2 = e
        mst2 = mst1.copy()
        subsets2 = copy.deepcopy(subsets1)

        while e2 < n - 1:
            if i == len(edges):
                return -1
            typ, u, v = edges[i]
            if typ != 2:
                break
            if find(subsets2, u) != find(subsets2, v):
                union(subsets2, u, v)
                mst2.add(u)
                mst2.add(v)
                e += 1
                e2 += 1
            i += 1

        if len(mst2) < n:
            return -1

        while e1 < n - 1:
            if i == len(edges):
                return -1

            typ, u, v = edges[i]
            if find(subsets1, u) != find(subsets1, v):
                union(subsets1, u, v)

                e += 1
                e1 += 1
            i += 1

        return len(edges) - e
