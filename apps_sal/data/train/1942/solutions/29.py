class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dic_companies = {}
        inx = 0
        for companies in favoriteCompanies:
            for company in companies:
                if company not in dic_companies:
                    dic_companies[company] = inx
                    inx += 1

        favorite_comp = []
        for companies in favoriteCompanies:
            val = 0
            for company in companies:
                val += 2 ** dic_companies[company]
            favorite_comp.append(val)

        res = []

        for i in range(len(favorite_comp)):
            flag = True
            for j in range(len(favorite_comp)):
                if i == j:
                    continue
                if favorite_comp[i] | favorite_comp[j] == favorite_comp[j]:
                    flag = False
                    break
            if flag:
                res.append(i)

        return res
