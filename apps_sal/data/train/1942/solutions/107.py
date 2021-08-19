class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sol = []
        for (i, curr_comps) in enumerate(favoriteCompanies):
            curr_comps = set(curr_comps)
            is_subset = False
            for (j, other_comps) in enumerate(favoriteCompanies):
                if j == i:
                    continue
                other_comps = set(other_comps)
                if curr_comps.issubset(other_comps):
                    is_subset = True
            if not is_subset:
                sol.append(i)
        return sol
