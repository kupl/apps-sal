class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        compfaves = {}

        for i, faves in enumerate(favoriteCompanies):
            for comp in faves:
                if not comp in compfaves:
                    compfaves[comp] = []
                compfaves[comp].append(i)

        outarr = []
        for i, faves in enumerate(favoriteCompanies):

            matches = {}
            for comp in faves:
                for person in compfaves[comp]:
                    if not person in matches:
                        matches[person] = 0
                    matches[person] += 1
            # print(i,matches)
            issubset = False
            for p, c in list(matches.items()):
                if len(faves) == c and p != i:
                    issubset = True
                    break
            if not issubset:
                outarr.append(i)
        return outarr
