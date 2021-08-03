def f(c):
    return ord(c) - ord('a')


class Solution:
    def wordSubsets(self, A, B):

        def isSubSet(coverA, coverB):
            for i in range(26):
                if coverA[i] < coverB[i]:
                    return False
            return True

        coverB = [0] * 26
        for b in B:
            cover = [0] * 26
            for c in b:
                cover[f(c)] += 1
            for i in range(26):
                coverB[i] = max(coverB[i], cover[i])

        res = []
        for a in A:
            coverA = [0] * 26
            for c in a:
                coverA[f(c)] += 1
            if isSubSet(coverA, coverB):
                res.append(a)
        return res
