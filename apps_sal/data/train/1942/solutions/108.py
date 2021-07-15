class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i in range(0, len(favoriteCompanies)): 
            setLst = set(favoriteCompanies[i])
            flag = False
            for j in range(0, len(favoriteCompanies)):
                if j == i:
                    continue 
                if setLst.issubset(set(favoriteCompanies[j])):
                    flag = True
                    break;
            if flag == False:
                ans.append(i)
        return ans
                    
                

