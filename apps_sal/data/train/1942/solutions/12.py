class Solution:

    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        fev_set = []
        for i in favoriteCompanies:
            tmp = set()
            for j in i:
                tmp.add(j)
            fev_set.append(tmp)
        ans = []
        for (ind, i) in enumerate(fev_set):
            flag = 0
            for (i2, j) in enumerate(fev_set):
                if i2 != ind and i <= j:
                    flag = 1
                    break
            if not flag:
                ans.append(ind)
        return ans
