class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        res = list(range(n))
        seen = set()
        for i in range(n - 1):
            for j in range(i + 1, n):
                first_set = set(favoriteCompanies[i])
                second_set = set(favoriteCompanies[j])
                remind = first_set & second_set

                if remind == first_set:
                    if i not in seen:
                        seen.add(i)
                        res.remove(i)
                if remind == second_set:
                    if j not in seen:
                        seen.add(j)
                        res.remove(j)
        return res
