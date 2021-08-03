class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        d = {i: set(favoriteCompanies[i]) for i in range(len(favoriteCompanies))}
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i != j:
                    if not d[i] - d[j]:
                        break
            else:
                ans.append(i)

        return ans
