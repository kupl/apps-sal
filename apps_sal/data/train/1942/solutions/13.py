class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        def isSubset(lst1, lst2):
            if len(lst1) > len(lst2):
                return False
            largerSet = set()
            for elt in lst2:
                largerSet.add(elt)
            for elt in lst1:
                if elt not in largerSet:
                    return False
            return True
        return [i for i in range(len(favoriteCompanies)) if not any((j != i and isSubset(favoriteCompanies[i], favoriteCompanies[j]) for j in range(len(favoriteCompanies))))]
