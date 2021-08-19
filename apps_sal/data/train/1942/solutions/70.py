class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        length = len(favoriteCompanies)
        for i in range(length):
            favoriteCompanies[i] = set(favoriteCompanies[i])
        res = []
        for i in range(length):
            pattern = favoriteCompanies[i]
            for flist in favoriteCompanies:
                if pattern < flist:
                    break
            else:
                res.append(i)
        return res
