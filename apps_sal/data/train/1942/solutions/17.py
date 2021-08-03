class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        no_overlap = []

        for i in range(len(favoriteCompanies)):
            flag = True
            for j in range(len(favoriteCompanies)):
                if i == j:
                    continue
                if len(set(favoriteCompanies[i]) - set(favoriteCompanies[j])) == 0:
                    flag = False
                    break

            if flag:
                no_overlap.append(i)

        return no_overlap
