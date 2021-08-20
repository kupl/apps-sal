class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fcs = [set(fc) for fc in favoriteCompanies]
        ret = []
        for i in range(len(fcs)):
            to_incl = True
            for j in range(len(fcs)):
                if j != i and fcs[i].issubset(fcs[j]):
                    to_incl = False
                    break
            if to_incl:
                ret.append(i)
        return ret
