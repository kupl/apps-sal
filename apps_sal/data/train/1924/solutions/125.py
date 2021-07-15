class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        l=[i.split(\",\") for i in transactions]
        n=len(transactions)
        valid=[True]*n
        for i in range(n):
            if int(l[i][2])>1000:
                valid[i]=False
        for i in range(n):
            for j in range(i+1,n):
                if valid[i] or valid[j]:
                    name1,time1,city1=l[i][0],l[i][1],l[i][3]
                    name2,time2,city2=l[j][0],l[j][1],l[j][3]
                    if name1==name2 and city1!=city2 and abs(int(time1)-int(time2))<=60:
                        valid[i],valid[j]=False,False
        return [transactions[i] for i in range(n) if not valid[i]]
