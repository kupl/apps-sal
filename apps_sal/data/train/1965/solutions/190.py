class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B = {i: i for i in range(1, n + 1)}, {i: i for i in range(1, n + 1)}
        #print(A, B)

        def find(dp, i):
            #print(i, dp)
            if dp[i] != i:
                dp[i] = find(dp, dp[i])
            return dp[i]
        edges = sorted(edges, reverse=True)

        cnt = 0
        for t, a, b in edges:
            if t == 3:
                if find(A, a) != find(A, b):
                    A[find(A, a)] = A[find(A, b)]
                    B[find(B, a)] = A[find(B, b)]
                else:
                    cnt += 1
            elif t == 2:
                if find(B, a) != find(B, b):
                    B[find(B, a)] = A[find(B, b)]
                else:
                    cnt += 1
            else:
                if find(A, a) != find(A, b):
                    A[find(A, a)] = A[find(A, b)]
                else:
                    cnt += 1
        return cnt if len(set(find(A, e) for e in range(1, n + 1))) == 1 and len(set(find(B, e) for e in range(1, n + 1))) == 1 else -1
