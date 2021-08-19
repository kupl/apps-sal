class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        comp_dict = {i: set(v) for (i, v) in enumerate(favoriteCompanies)}
        for i in range(len(favoriteCompanies)):
            subset = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if not comp_dict[i] - comp_dict[j]:
                    subset = False
                    break
            if subset:
                res.append(i)
        return res
