class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        l = [0] * len(favoriteCompanies)
        p = []
        for i in range(len(favoriteCompanies)):

            if l[i] == 0:
                p.append(i)
                temp = set(favoriteCompanies[i])
                for j in range(i + 1, len(favoriteCompanies)):
                    if temp & set(favoriteCompanies[j]) == temp:
                        l[i] = 1

                        p[-1] = j
                        temp = set(favoriteCompanies[j])
                    elif temp & set(favoriteCompanies[j]) == set(favoriteCompanies[j]):
                        l[j] = 1

        p = set(p)
        p = list(p)
        p.sort()
        return p
