class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        in_val = []
        trans = []
        for each in transactions:
            temp = each
            temp = temp.split(\",\")
            trans.append(temp)
        #print(trans)
        
        size = len(trans)
        for i in range(size):
            if int(trans[i][2]) > 1000:
                if transactions[i] not in in_val:
                    in_val.append(transactions[i])
            else:
                for j in range(size):
                    if i != j and trans[i][0] == trans[j][0] and abs(int(trans[i][1])-int(trans[j][1])) <= 60 and trans[i][3] != trans[j][3]:
                        if transactions[i] not in in_val:
                            in_val.append(transactions[i])
        return in_val
        
        
        
        
        
