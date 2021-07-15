class Solution:
    def maxNumEdgesToRemove(self, N: int, E: List[List[int]], same = 0) -> int:
        E = [[_, u - 1, v - 1] for _, u, v in E]                    # ⭐️ -1 for 1-based to 0-based indexing
        A = [i for i in range(N)]                                   # \\U0001f642 parent representatives of disjoint sets for Alice
        B = [i for i in range(N)]                                   # \\U0001f642 parent representatives of disjoint sets for Bob
        def find(P, x): P[x] = P[x] if P[x] == x else find(P, P[x]); return P[x]
        def union(P, a, b):
            a = find(P, a)
            b = find(P, b)
            if a == b:
                return 1
            P[a] = b  # arbitrary choice
            return 0
        for type, u, v in E:
            if type == 3: same += union(A, u, v) | union(B, u, v)   # \\U0001f947 first: \\U0001f517 union ✅ shared edges between Alice and Bob
        for type, u, v in E:
            if type == 1: same += union(A, u, v)                    # \\U0001f948 second: \\U0001f517 union \\U0001f6ab non-shared edges between Alice and Bob
            if type == 2: same += union(B, u, v)
        return same if all(find(A, 0) == find(A, x) for x in A) and all(find(B, 0) == find(B, x) for x in B) else -1
        

