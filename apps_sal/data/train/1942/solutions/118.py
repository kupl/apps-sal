class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        res = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                first_set = set(favoriteCompanies[i])
                second_set = set(favoriteCompanies[j])
                remind = first_set & second_set
                if remind == first_set:
                    res.add(i)
                if remind == second_set:
                    res.add(j)
        return sorted(list(set(range(n)) - res))
