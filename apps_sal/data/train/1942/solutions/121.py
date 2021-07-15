class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        company = []
        for i, fc in enumerate(favoriteCompanies):
            company.append((tuple(fc), len(fc), i))
        company.sort(key = lambda x: -x[1])
        
        maxlen = company[0][1]
        loc = -1
        res= []
        for i in range(len(company)):
            if company[i][1] == maxlen:
                res.append(company[i][2])
                loc= max(loc, i)
            else: break
        
        for i in range(loc+1, len(company)):
            curr = company[i][0]
            flag = 0
            for j in range(i-1, -1, -1):
                tmpt = company[j][0]
                if set(curr) & set(tmpt) == set(curr): flag = 1
            if flag == 0: res.append(company[i][2])
        return sorted(res)
                
                
                

            

