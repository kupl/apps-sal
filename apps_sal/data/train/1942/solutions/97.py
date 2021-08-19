class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        hms = []
        output = []
        for favs in favoriteCompanies:
            hm = set(favs)
            hms.append(hm)
        for i in range(len(favoriteCompanies)):
            good = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                z = hms[j].intersection(hms[i])
                if z == hms[i]:
                    good = False
            if good:
                output.append(i)
        return output
