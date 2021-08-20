from collections import defaultdict


class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bMap = defaultdict(int)
        ans = []
        maxB = [0] * 26
        for b in B:
            m = self.count(b)
            for i in range(len(m)):
                maxB[i] = max(maxB[i], m[i])
        for a in A:
            aMap = self.count(a)
            c = 0
            for i in range(len(aMap)):
                if aMap[i] >= maxB[i]:
                    c += 1
            if c == 26:
                ans.append(a)
        return ans

    def count(self, arr):
        ans = [0] * 26
        for ch in arr:
            ans[ord(ch) - ord('a')] += 1
        return ans
