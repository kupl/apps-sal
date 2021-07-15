class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fav = []
        for f in favoriteCompanies:
            fav.append(set(f))

        n = len(favoriteCompanies)
        rem = set()

        for i in range(n):
            for j in range(i+1, n):
                if not fav[i] - fav[j]: # then i is a subset of j
                    rem.add(i)
                if not fav[j] - fav[i]:
                    rem.add(j)

        res = []
        for i in range(n):
            if i not in rem:
                res.append(i)

        return res
