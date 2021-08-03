class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)

        for i in range(n):
            favoriteCompanies[i] = set(favoriteCompanies[i])

        ans = []

        for i in range(n):
            for j in range(n):
                if i != j and favoriteCompanies[i] <= favoriteCompanies[j]:
                    break
            else:
                ans.append(i)

        return ans
