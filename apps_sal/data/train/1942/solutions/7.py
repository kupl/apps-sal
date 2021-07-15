class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        \"\"\"
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        \"\"\"
        noSubset = []
        # print(len(favoriteCompanies))
        for i in range(len(favoriteCompanies)):
            people = favoriteCompanies.copy()
            people.pop(i)
            # print(i)
            # print(favoriteCompanies)
            index = favoriteCompanies[i]
            subsetStatus = [set(index).issubset(set(x)) for x in people]
            if any(subsetStatus) == True:
                # print(\"True\")
                continue
            else:
                # print('False')
                noSubset.append(i)
        return noSubset 
