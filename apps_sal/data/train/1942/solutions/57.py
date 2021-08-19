class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = favoriteCompanies[:]
        for i in range(len(companies)):
            companies[i] = set(companies[i])
        subsets = []
        for i in range(len(companies)):
            currSet = companies[i]
            for j in range(len(companies)):
                if i != j:
                    count = 0
                    for each in currSet:
                        if each in companies[j]:
                            count += 1
                        else:
                            break
                    if count == len(currSet):
                        subsets.append(i)
                        break
        size = len(favoriteCompanies) - len(subsets)
        res = [None] * size
        curr = 0
        subsets = set(subsets)
        for i in range(len(favoriteCompanies)):
            if i not in subsets:
                res[curr] = i
                curr += 1
        return res
