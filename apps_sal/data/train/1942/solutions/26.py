class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i in range(len(favoriteCompanies)):
            flag = 0
            for j in range(len(favoriteCompanies)):
                if set(favoriteCompanies[i]) & set(favoriteCompanies[j]) == set(favoriteCompanies[i]) and i != j:
                    flag = 1
                    break
            if flag == 0:
                ans.append(i)
        return ans
