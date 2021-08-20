class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dict = defaultdict(int)
        for (i, lst) in enumerate(favoriteCompanies):
            people_mask = 1 << i
            for comp in lst:
                dict[comp] += people_mask
        res = []
        for (i, lst) in enumerate(favoriteCompanies):
            other_people = ~(1 << i)
            for comp in lst:
                other_people &= dict[comp]
                if not other_people:
                    break
            if not other_people:
                res.append(i)
        return res
