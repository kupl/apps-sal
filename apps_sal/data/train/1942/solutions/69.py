class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies_set = [set(c) for c in favoriteCompanies]
        res = []
        for (i, s1) in enumerate(companies_set):
            is_subset = False
            for (j, s2) in enumerate(companies_set):
                if i == j:
                    continue
                if s1.issubset(s2):
                    is_subset = True
            if not is_subset:
                res.append(i)
        return res
