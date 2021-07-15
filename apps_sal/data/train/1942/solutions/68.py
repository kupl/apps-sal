class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        res = list(range(n))
        seen = set()
        array_of_sets = [set(company) for company in favoriteCompanies]
        for i in range(n-1):
            for j in range(i+1, n):
                if i != j:
                    remind = array_of_sets[i] & array_of_sets[j]
                    if remind == array_of_sets[i]:
                        if i not in seen:
                            seen.add(i)
                            res.remove(i)
                    if remind == array_of_sets[j]:
                        if j not in seen:
                            seen.add(j)
                            res.remove(j)
        return res

