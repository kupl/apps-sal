import collections


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dp = [0] * 26
        for b in B:
            dp = [max(i, j) for i, j in zip(dp, self.bow(b))]
        print(dp)
            
        res = []
        for a in A:
            if not any([al < bl for al, bl in zip(self.bow(a), dp)]):
                res.append(a)
        return res
    
    def bow(self, text):
        d = [0] * 26
        for l in text:
            d[ord(l) - ord('a')] += 1
        return d
