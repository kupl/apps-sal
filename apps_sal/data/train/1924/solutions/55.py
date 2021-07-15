class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        # transactions = [i.split(\",\") for i in transactions]
        # transactions.sort(key = lambda x:(x[0],int(x[1])))
        # temp = transactions[0]
        # if int(temp[2])>1000:
        #     invalid.add(\",\".join(temp))
        # for i in transactions[1:]:
        #     if int(i[2])>1000:
        #         invalid.add(\",\".join(i))
        #         if i[0]==temp[0] and i[3]!=temp[3] and (int(i[1])-int(temp[1]))<=60:
        #             invalid.add(\",\".join(temp))
        #         temp = i
        #     elif i[0]==temp[0] and i[3]!=temp[3] and (int(i[1])-int(temp[1]))<=60:
        #         invalid.add(\",\".join(temp))
        #         invalid.add(\",\".join(i))
        #         temp = i
        #     else:
        #         temp = i        
        # return invalid
        
        for ind,val in enumerate(transactions):
            temp = val.split(\",\")
            if int(temp[2])>1000:
                invalid.add(val)
            for ind2 in range(ind+1, len(transactions)):
                temp2 = transactions[ind2].split(\",\")
                if temp2[0]==temp[0] and temp2[3]!=temp[3] and abs(int(temp2[1])-int(temp[1]))<=60:
                    invalid.add(transactions[ind2])
                    invalid.add(val)
        return invalid           
                
                
            
            
