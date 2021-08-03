class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:

        htable = {}
        for i, j in enumerate(favoriteCompanies):
            htable[i] = set(j)
        result = []
        for k in htable:
            flag = True
            for j in list(htable.values()):
                if htable[k] == j:
                    continue
                elif htable[k].issubset(j):
                    flag = False
                    break

            if flag:
                result.append(k)
        print(result)
        return result
