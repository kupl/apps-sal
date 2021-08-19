class Solution:

    def count(self, word):
        res = [0] * 26
        for item in word:
            tmp = ord(item) - ord('a')
            res[tmp] += 1
        return res

    def satisfy(self, item, bmax):
        tmp = self.count(item)
        for i in range(26):
            if tmp[i] < bmax[i]:
                return False
        return True

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bmax = [0] * 26
        for item in B:
            for (index, val) in enumerate(self.count(item)):
                bmax[index] = max(bmax[index], val)
        res = []
        for item in A:
            if self.satisfy(item, bmax):
                res.append(item)
        return res
