class Solution:
    def maxNumEdgesToRemove(self, N: int, E: List[List[int]], same=0) -> int:
        E = [[_, u - 1, v - 1] for _, u, v in E]
        A = [i for i in range(N)]
        B = [i for i in range(N)]
        def find(P, x): P[x] = P[x] if P[x] == x else find(P, P[x]); return P[x]

        def union(P, a, b):
            a = find(P, a)
            b = find(P, b)
            if a == b:
                return 1
            P[a] = b
            return 0
        for type, u, v in E:
            if type == 3:
                same += union(A, u, v) | union(B, u, v)
        for type, u, v in E:
            if type == 1:
                same += union(A, u, v)
            if type == 2:
                same += union(B, u, v)
        parentA = find(A, 0)
        parentB = find(B, 0)
        return same if all(parentA == find(A, x) for x in A) and all(parentB == find(B, x) for x in B) else -1
