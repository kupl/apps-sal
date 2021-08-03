class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        res = list(range(n))
        array_of_sets = [set(company) for company in favoriteCompanies]
        for i in range(n):
            for j in range(n):
                if i != j:
                    if array_of_sets[i].issubset(array_of_sets[j]):
                        res.remove(i)
                        break

        return res
