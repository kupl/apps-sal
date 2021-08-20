class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        root = [-1] * (n + 1)
        ans = 0

        def getroot(u):
            while root[u] >= 0:
                u = root[u]
            return u

        def union(u, v):
            t = root[u] + root[v]
            if root[u] < root[v]:
                root[v] = u
                root[u] = t
            else:
                root[v] = t
                root[u] = v
        for (t, u, v) in edges:
            if t != 3:
                continue
            rootu = getroot(u)
            rootv = getroot(v)
            if rootu == rootv:
                ans += 1
            else:
                union(rootu, rootv)
        temp_root = list(root)
        for (t, u, v) in edges:
            if t != 1:
                continue
            rootu = getroot(u)
            rootv = getroot(v)
            if rootu == rootv:
                ans += 1
            else:
                union(rootu, rootv)
        if root.count(-1) > 1:
            return -1
        root = list(temp_root)
        for (t, u, v) in edges:
            if t != 2:
                continue
            rootu = getroot(u)
            rootv = getroot(v)
            if rootu == rootv:
                ans += 1
            else:
                union(rootu, rootv)
        if root.count(-1) > 1:
            return -1
        return ans
