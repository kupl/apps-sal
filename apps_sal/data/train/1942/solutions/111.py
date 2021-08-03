class Solution:
    def isSub(self, s1, s2):
        i = 0
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                i = i + 1
            if i == len(s1):
                return True
        return False

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fc = [(sorted(e), i) for i, e in enumerate(favoriteCompanies)]
        fc = sorted(fc, key=lambda x: len(x[0]), reverse=True)
        # print(fc)
        res = []
        for i in range(len(fc)):
            s, si = fc[i]
            found = False
            for j in range(i):
                ps, sj = fc[j]
                if self.isSub(s, ps):
                    found = True
                    break
            if not found:
                res.append(si)

        return sorted(res)
