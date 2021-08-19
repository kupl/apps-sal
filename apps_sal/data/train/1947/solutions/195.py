import collections


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        A = [(a, collections.Counter(a)) for a in A]
        newB = {}
        for b in B:
            for (x, c) in collections.Counter(b).items():
                newB[x] = c if x not in newB else max(newB[x], c)
        B = newB
        ans = []
        for (a, counts) in A:
            allMatch = True
            for (x, c) in B.items():
                if counts[x] < c:
                    allMatch = False
                    break
            if allMatch:
                ans.append(a)
        return ans
