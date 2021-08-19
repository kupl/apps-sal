def comp(a, b):
    for i in a:
        if(i not in b):
            return 0
    return 1


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        favoriteCompanies = [(j, i) for i, j in enumerate(favoriteCompanies)]
        x = sorted(favoriteCompanies, key=lambda x: len(x[0]), reverse=True)
        y = [i[1] for i in x]
        x = [i[0] for i in x]
        arrd = []
        for i in range(len(x)):
            d = {}
            for j in range(len(x[i])):
                d[x[i][j]] = 1
            arrd.append(d)
        # print(arrd)
        ind = [0] * len(x)
        for j in range(len(x)):
            for i in range(j - 1, -1, -1):
                if(comp(arrd[j], arrd[i])):
                    ind[j] = 1
                    break
        f = []
        for i in range(len(ind)):
            if(ind[i] == 0):
                f.append(y[i])
        return sorted(f)
