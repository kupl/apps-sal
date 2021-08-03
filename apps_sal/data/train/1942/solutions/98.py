class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        favoriteCompanies = [set(elem) for elem in favoriteCompanies]

        ans = []
        for i in range(n):
            not_subset = True
            for j in range(n):
                if i == j:
                    continue
                if len(favoriteCompanies[i] - favoriteCompanies[j]) == 0:
                    not_subset = False
                    break
            if not_subset:
                ans.append(i)
        return ans
