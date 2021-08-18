from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        pref = defaultdict(set)
        for dis in dislikes:
            a, b = dis
            pref[a].add(b)
            pref[b].add(a)

        to_visit = set(range(1, N + 1))

        while to_visit:
            cur = to_visit.pop()

            if cur not in pref:
                pass
            else:

                r1 = set([cur])
                r2 = pref[cur]
                L1 = r2.copy()
                L2 = set()

                while L1:
                    for l in L1:
                        to_visit.remove(l)
                        L = pref[l]
                        if l in r1:
                            if L.intersection(r1):
                                return False
                            else:
                                r2 = r2.union(L)
                        if l in r2:
                            if L.intersection(r2):
                                return False
                            else:
                                r1 = r1.union(L)
                        L2 = L2.union(L)
                    L2 = L2.intersection(to_visit)
                    L1 = L2
                    L2 = set()
        return True
