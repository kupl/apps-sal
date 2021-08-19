class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        (t1, t2, t3) = ([], [], [])
        for (t, s, e) in edges:
            if t == 1:
                t1.append([s, e])
            elif t == 2:
                t2.append([s, e])
            elif t == 3:
                t3.append([s, e])

        def find(x, arr):
            if x == arr[x]:
                return x
            else:
                arr[x] = find(arr[x], arr)
                return arr[x]
        ans = 0
        (alice, bob) = ([i for i in range(n + 1)], [i for i in range(n + 1)])
        for (s, e) in t3:
            (g1, g2) = (find(s, alice), find(e, alice))
            if g1 != g2:
                alice[g1] = g2
                bob[g1] = g2
            else:
                ans += 1
        for (s, e) in t1:
            (g1, g2) = (find(s, alice), find(e, alice))
            if g1 != g2:
                alice[g1] = g2
            else:
                ans += 1
        for (s, e) in t2:
            (g1, g2) = (find(s, bob), find(e, bob))
            if g1 != g2:
                bob[g1] = g2
            else:
                ans += 1
        root1 = find(alice[1], alice)
        for i in range(1, len(alice)):
            if find(i, alice) != root1:
                return -1
        root2 = find(bob[1], bob)
        for i in range(1, len(bob)):
            if find(i, bob) != root2:
                return -1
        return ans
