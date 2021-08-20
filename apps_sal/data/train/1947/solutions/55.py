from collections import defaultdict


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        result = []
        if not A:
            return result
        if not B:
            return A
        C = []
        for j in B:
            d = [0] * 26
            for ch in j:
                d[ord(ch) - ord('a')] += 1
            C.append(d)
        l = [0] * 26
        for j in C:
            for i in range(26):
                l[i] = max(l[i], j[i])
        for i in A:
            d = list(l)
            for ch in i:
                if d[ord(ch) - ord('a')] > 0:
                    d[ord(ch) - ord('a')] -= 1
            if sum(d) == 0:
                result.append(i)
        return result
