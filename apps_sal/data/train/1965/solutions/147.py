class Solution:
    def num_components(self, n, edges):
        parents = [0 for _ in range(n+1)]
        components = n
        def root(u):
            if parents[u] == 0:
                return u
            r = root(parents[u])
            parents[u] = r
            return r
        for u, v in edges:
            a, b = root(u), root(v)
            if a == b:
                continue
            else:
                components -= 1
                parents[a] = b
        return components
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = [edge[1:] for edge in edges if edge[0] == 1]
        B = [edge[1:] for edge in edges if edge[0] == 2]
        C = [edge[1:] for edge in edges if edge[0] == 3]
        a = self.num_components(n, A + C)
        b = self.num_components(n, B + C)
        c = self.num_components(n, C)
        #print(f'a={a}, b={b}, c={c}')
        if a > 1 or b > 1:
            return -1
        deleted_common_edges = len(C) - n + c
        deleted_alice_edges = len(A) + len(C) - n + 1 - deleted_common_edges
        deleted_bob_edges = len(B) + len(C) - n + 1 - deleted_common_edges
        #print(deleted_common_edges, deleted_alice_edges, deleted_bob_edges)
        return deleted_common_edges + deleted_alice_edges + deleted_bob_edges
