class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        l = len(favoriteCompanies)
        for i in range(l):
            f = 0
            for j in range(l):
                if i != j:
                    if (set(favoriteCompanies[i]) | set(favoriteCompanies[j])) == set(favoriteCompanies[j]):
                        f = 1
                        break
            if f == 0:
                res.append(i)
        return res
