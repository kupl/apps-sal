class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=set()
        for i in range(len(transactions)):
            name1,time1,amount1,city1=transactions[i].split(\",\")
            if int(amount1)> 1000:
                invalid.add(transactions[i])
            for j in range(i+1,len(transactions)):
                name2,time2,amount2,city2=transactions[j].split(\",\")
                if name1 == name2 and abs(int(time1)-int(time2)) <= 60 and city1!=city2:
                            invalid.add(transactions[i])
                            invalid.add(transactions[j])
        return list(invalid)
