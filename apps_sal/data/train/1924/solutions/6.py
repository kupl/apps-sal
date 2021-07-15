class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        temp=[]       
        for t in transactions:
            temp.append(t.split(','))
        temp=sorted(temp, key=lambda x: x[0])  
        
        res=set()
        for i in range(len(temp)):
            if int(temp[i][2])>1000:
                res.add(','.join(temp[i]))
            for j in range(i+1, len(temp)):
                if temp[i][0]==temp[j][0] and temp[i][3]!=temp[j][3] and abs(int(temp[i][1])-int(temp[j][1]))<=60:
                            res.add(','.join(temp[i]))
                            res.add(','.join(temp[j]))
                
                
        return res
            

