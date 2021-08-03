class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        for ind,trn in enumerate(transactions):
            name,time,amt,city = trn.split(\",\")
            if int(amt)>1000:
                invalid.append(trn)
                continue
            for j,trn2 in enumerate(transactions):
                if ind!=j:
                    name1,time1,amt1,city1 = trn2.split(\",\")
                    if name==name1 and abs(int(time)-int(time1))<=60 and city!=city1:
                        invalid.append(trn)
                        break
        return invalid
