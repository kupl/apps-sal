class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parenta = [x for x in range(n + 1)]
        parentb = [x for x in range(n + 1)]

        def ufind(parent, x):
            if parent[x] != x:
                parent[x] = ufind(parent, parent[x])
            return parent[x]

        def uunion(parent, a, b):
            ua = ufind(parent, a)
            ub = ufind(parent, b)

            parent[ua] = ub

        edges.sort(key=lambda x: (-x[0]))

        count = 0
        for t, u, v in edges:
            if t == 3:
                if ufind(parenta, u) != ufind(parenta, v) or ufind(parentb, u) != ufind(parentb, v):
                    uunion(parenta, u, v)
                    uunion(parentb, u, v)
                else:
                    count += 1
            elif t == 2:
                if ufind(parentb, u) != ufind(parentb, v):
                    uunion(parentb, u, v)
                else:
                    count += 1
            else:
                if ufind(parenta, u) != ufind(parenta, v):
                    uunion(parenta, u, v)
                else:
                    count += 1

        roota = ufind(parenta, 1)
        rootb = ufind(parentb, 1)
        for x in range(1, n + 1):
            if ufind(parenta, x) != roota or ufind(parentb, x) != rootb:
                return -1

        return count
