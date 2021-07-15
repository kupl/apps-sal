class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        result = []
        fcSet = [set(fc) for fc in favoriteCompanies]
        n = len(favoriteCompanies)
        for i, fcs1 in enumerate(fcSet):
            for j, fcs2 in enumerate(fcSet):
                if i==j:
                    continue
                if fcs1<fcs2:
                    break
            else:
                result.append(i)
        return result
