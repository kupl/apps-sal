class Solution:
    def combineString(self,lis):
        ans=\"\"
        for i in range(len(lis)):
            ans=ans+lis[i]
        return ans
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ftran=[]
        findex=set()
        name=[]
        time=[]
        amt=[]
        city=[]
        for i in range(len(transactions)):
            a,b,c,d=transactions[i].split(\",\")
            name.append(self.combineString(a))
            e=int(self.combineString(b))
            time.append(e)
            amt.append(self.combineString(c))
            city.append(self.combineString(d))
        for i in range(len(transactions)):
            s=self.combineString(amt[i])
            t=int(s)
            if t>1000:
                findex.add(i)
        for i in range(len(name)):
            for j in range(len(name)):
                if i==j:
                    continue
                if name[i]==name[j] and abs(time[i]-time[j])<=60 and city[i]!=city[j]:
                    findex.add(i)
                    findex.add(j)
        findexl=list(findex)
        for i in range(len(findexl)):
            ftran.append(transactions[findexl[i]])
        return ftran
                    
            
            
                
            
        
    

