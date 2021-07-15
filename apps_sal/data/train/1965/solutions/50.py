class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        edges = sorted(edges, reverse=True)
        alice, bob = [i for i in range(n + 1)], [i for i in range(n + 1)]
        size_alice, size_bob = [1 for i in range(n + 1)], [1 for i in range(n + 1)]
        ans = 0
        
        def find(u, state):
            if state == \"a\":
                if alice[u] == u:
                    return u
                return find(alice[u], state)
            else:
                if bob[u] == u:
                    return u
                return find(bob[u], state)
            
        
        def union(u, v, state):
            nonlocal ans
            
            add = 0
            if state == 3 or state == 1:
                p1, p2 = find(u, \"a\"), find(v, \"a\")
                if p1 != p2:
                    add = 1
                    print(\"haha\", u, v)
                    if size_alice[p1] >= size_alice[p2]:
                        size_alice[p1] += size_alice[p2]
                        alice[p2] = p1
                    else:
                        size_alice[p2] += size_alice[p1]
                        alice[p1] = p2

            if state == 3 or state == 2:
                p1, p2 = find(u, \"b\"), find(v, \"b\")
                if p1 != p2:
                    add = 1
                    print(\"haha\", u, v)
                    if size_bob[p1] >= size_bob[p2]:
                        size_bob[p1] += size_bob[p2]
                        bob[p2] = p1
                    else:
                        size_bob[p2] += size_bob[p1]
                        bob[p1] = p2
            ans += add
                
        
        for t,u,v in edges:
            union(u, v, t)
        # print(size_alice, size_bob)
        if max(size_alice) != n or max(size_bob) != n:
            return -1
        return len(edges) - ans
