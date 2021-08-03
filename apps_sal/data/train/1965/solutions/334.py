class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        d = [[], [], []]
        for type, u, v in edges:
            d[type - 1].append((u - 1, v - 1))

        parent = list(range(n))

        def find(x, l):
            if x != l[x]:
                l[x] = find(l[x], l)
            return l[x]

        cnt = 0
        for u, v in d[-1]:
            ru, rv = find(u, parent), find(v, parent)
            if ru != rv:
                parent[ru] = rv
                cnt += 1

        alice = [num for num in parent]
        for u, v in d[0]:
            ru, rv = find(u, alice), find(v, alice)
            if ru != rv:
                alice[ru] = rv
                cnt += 1

        ra = find(0, alice)
        for i in range(n):
            if find(i, alice) != ra:
                return -1

        bob = [num for num in parent]
        for u, v in d[1]:
            ru, rv = find(u, bob), find(v, bob)
            if ru != rv:
                bob[ru] = rv
                cnt += 1

        rb = find(0, bob)
        for i in range(n):
            if find(i, bob) != rb:
                return -1

        return len(edges) - cnt
