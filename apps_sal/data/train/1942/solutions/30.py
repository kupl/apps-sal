class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []

        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i != j:
                    if len(set(favoriteCompanies[i]) & set(favoriteCompanies[j])) == len(set(favoriteCompanies[i])):
                        break
            else:
                ans.append(i)
        return ans
