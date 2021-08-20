from collections import defaultdict


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(list)
        for (t, u, v) in edges:
            d[t].append((u - 1, v - 1))
        (bob, alice) = (list(range(n)), list(range(n)))

        def find(x, is_bob):
            if is_bob:
                if x != bob[x]:
                    bob[x] = find(bob[x], is_bob)
                return bob[x]
            else:
                if x != alice[x]:
                    alice[x] = find(alice[x], is_bob)
                return alice[x]
        res = 0
        for t in [3, 2, 1]:
            for (u, v) in d[t]:
                if t == 3:
                    (rootu, rootv) = (find(u, True), find(v, True))
                    if rootu != rootv:
                        bob[rootu] = rootv
                        alice[rootu] = rootv
                        res += 1
                elif t == 1:
                    (rootu, rootv) = (find(u, False), find(v, False))
                    if rootu != rootv:
                        alice[rootu] = rootv
                        res += 1
                else:
                    (rootu, rootv) = (find(u, True), find(v, True))
                    if rootu != rootv:
                        bob[rootu] = rootv
                        res += 1
        (root_bob, root_alice) = (find(0, True), find(0, False))
        if all((find(num, True) == root_bob for num in bob)) and all((find(num, False) == root_alice for num in alice)):
            return len(edges) - res
        else:
            return -1
