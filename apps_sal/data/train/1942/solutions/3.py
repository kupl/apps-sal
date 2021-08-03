
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        result = []
        for x in range(0, len(favoriteCompanies)):
            flag = True
            for y in range(0, len(favoriteCompanies)):
                if x == y:
                    continue

                setx = set(favoriteCompanies[x])
                sety = set(favoriteCompanies[y])

                if setx.issubset(sety):

                    flag = False
                    break

            if flag:
                result.append(x)

        return sorted(result)
