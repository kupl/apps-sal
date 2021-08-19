class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [[len(favoriteCompanies[i]), i, set(favoriteCompanies[i])] for i in range(len(favoriteCompanies))]
        favoriteCompanies.sort()
        # print(favoriteCompanies)
        res = []
        for i in range(len(favoriteCompanies)):
            attendre = favoriteCompanies[i][2]
            flag = True
            for j in range(i + 1, len(favoriteCompanies)):
                if not attendre - favoriteCompanies[j][2]:
                    flag = False
                    break
            if flag:
                res.append(favoriteCompanies[i][1])
        return sorted(res)
