class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        d = {i: set(v) for (i, v) in enumerate(favoriteCompanies)}
        print(d)
        res = []
        for i in range(len(favoriteCompanies)):
            subSet = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if not d[i] - d[j]:
                    subSet = False
                    break
            if subSet:
                res.append(i)
        return res
