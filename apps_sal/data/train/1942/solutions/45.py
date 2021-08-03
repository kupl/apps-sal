class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        cs = {w for f in favoriteCompanies for w in f}
        cs = {v: i for i, v in enumerate(cs)}
        fs = []
        for f in favoriteCompanies:
            i = 0
            for c in f:
                i |= 1 << cs[c]
            fs.append(i)

        ans = []
        for i in range(len(fs)):
            f = 1
            for j in range(len(fs)):
                if i == j:
                    continue
                if fs[i] | fs[j] == fs[j]:
                    f ^= 1
                    break
            if f:
                ans.append(i)
        return ans
