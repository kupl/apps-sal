class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        coms = sorted([[set(cs), oi] for (oi, cs) in enumerate(favoriteCompanies)], key=lambda x: len(x[0]))
        ret = []
        for (i, com) in enumerate(coms):
            (com1, oi) = com
            is_sub = False
            for (com2, _) in coms[i + 1:]:
                if not com1 - com2:
                    is_sub = True
                    break
            if not is_sub:
                ret.append(oi)
        return sorted(ret)
