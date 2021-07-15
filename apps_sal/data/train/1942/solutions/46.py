class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        subsets = sorted([[set(companies), i]
                            for i, companies in enumerate(favoriteCompanies)], key=lambda x: len(x[0]))
        for i, companies in enumerate(subsets):
            companies, res_i = companies
            for j, companies2 in enumerate(subsets[i+1:], i+1):
                companies2 = companies2[0]
                if all(company in companies2 for company in companies):
                    break
            else:
                res += res_i,
        return sorted(res)
