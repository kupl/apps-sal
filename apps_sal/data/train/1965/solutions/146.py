class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        roots1 = [i for i in range(n + 1)]
        roots2 = [i for i in range(n + 1)]

        def find_root(roots, i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        ans = 0
        edges.sort(reverse=True)
        for edge in edges:
            if edge[0] == 3:
                if find_root(roots1, edge[1]) == find_root(roots1, edge[2]) and find_root(roots2, edge[1]) == find_root(roots2, edge[2]):
                    ans += 1
                else:
                    roots1[find_root(roots1, edge[2])] = find_root(roots1, edge[1])
                    roots2[find_root(roots2, edge[2])] = find_root(roots2, edge[1])
            elif edge[0] == 1:
                if find_root(roots1, edge[1]) == find_root(roots1, edge[2]):
                    ans += 1
                else:
                    roots1[find_root(roots1, edge[2])] = find_root(roots1, edge[1])
            elif find_root(roots2, edge[1]) == find_root(roots2, edge[2]):
                ans += 1
            else:
                roots2[find_root(roots2, edge[2])] = find_root(roots2, edge[1])
        g1 = set()
        for i in range(1, len(roots1)):
            g1.add(find_root(roots1, i))
        if len(g1) > 1:
            return -1
        g2 = set()
        for i in range(1, len(roots2)):
            g2.add(find_root(roots2, i))
        if len(g2) > 1:
            return -1
        return ans
