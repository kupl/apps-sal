class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for i in word:
                ans[ord(i) - ord('a')] += 1
            return ans
        bMax = [0] * 26
        for b in B:
            ls = count(b)
            for c in range(26):
                bMax[c] = max(bMax[c], ls[c])
        res = []
        for i in A:
            ls = count(i)
            for c in range(26):
                if ls[c] < bMax[c]:
                    break
            else:
                res += [i]
        return res
