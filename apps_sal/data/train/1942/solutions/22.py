class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        subsets = set()
        res = []
        for i in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if i != j and set(favoriteCompanies[i]).issubset(favoriteCompanies[j]):
                    subsets.add(i)
        for i in range(len(favoriteCompanies)):
            if i not in subsets:
                res.append(i)
        return res
