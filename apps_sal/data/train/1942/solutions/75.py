from collections import defaultdict


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        out = []
        d = defaultdict(list)
        for i, companies in enumerate(favoriteCompanies):
            for company in companies:
                d[company].append(i)
        for i, companies in enumerate(favoriteCompanies):
            s = set(d[companies[0]])
            for company in companies:
                s = s.intersection(d[company])
            if len(s) == 1:
                out.append(i)
        return out
