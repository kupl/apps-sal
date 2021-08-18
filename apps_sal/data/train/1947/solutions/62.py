class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            res = [0] * 26
            for i in word:
                res[ord(i) - ord('a')] += 1
            return res
        b_max = [0] * 26
        for b in B:
            bb = count(b)
            for w in range(26):
                b_max[w] = max(b_max[w], bb[w])
        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), b_max)):
                ans.append(a)
        return ans
