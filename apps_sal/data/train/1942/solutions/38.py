class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(x) for x in favoriteCompanies]
        for (i, companies) in enumerate(sets):
            for (j, other) in enumerate(sets):
                if i == j:
                    continue
                if companies <= other:
                    break
            else:
                yield i
