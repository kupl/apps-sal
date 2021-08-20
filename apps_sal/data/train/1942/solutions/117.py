class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        yu = []
        for j in range(len(favoriteCompanies)):
            a = favoriteCompanies[j]
            yu1 = list(favoriteCompanies)
            yu1.pop(j)
            if any((set(a).issubset(set(ele)) for ele in yu1)) == False:
                yu.append(j)
        return yu
