class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # favoriteCompanies=sorted(favoriteCompanies,key=lambda x:len(x))
        
        ls=[]
        for i in favoriteCompanies:
            ls.append(set(i))
        
        # print(ls)
        ans=[]
        for i in range(len(ls)):
            flag=0
            for j in range(len(ls)):
                if(i!=j):
                    tem=ls[i].intersection(ls[j])
                    if(tem==ls[i]):
                        flag=1
                        break

                
            if(flag==0):
                ans.append(i)
                
        return ans
