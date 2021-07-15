class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        dic = {}
        ind = 0
        profile = []
        for companies in favoriteCompanies:
            for company in companies:
                if company not in dic:
                    dic[company] = ind
                    ind += 1
        
        for companies in favoriteCompanies:
            val = 0
            for company in companies:
                val += 2**dic[company]
            profile.append(val)
        
        res = []
        for i in range(len(profile)):
            flag = True
            for j in range(len(profile)):
                if i == j:
                    continue
                elif profile[i] | profile[j] == profile[j]:
                    flag = False
                    break
            if flag:
                res.append(i)
        return res

