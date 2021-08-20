class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        lst = []
        n = len(favoriteCompanies)
        for i in range(n):
            c = set(favoriteCompanies[i])
            lst.append([c, i])
        lst.sort(key=lambda x: -len(x[0]))
        subset = set()
        for i in range(n - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if lst[j][0] & lst[i][0] == lst[i][0]:
                    subset.add(lst[i][1])
        return [i for i in range(n) if i not in subset]
