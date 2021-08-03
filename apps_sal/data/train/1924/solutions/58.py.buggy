class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ret = []
        leng = len(transactions)
        sorted_trans = sorted(transactions, key = lambda i: int(i.split(\",\", 3)[1]))
        print(sorted_trans)
        for i, trans in enumerate(sorted_trans):
            name, time, amount, city = trans.split(\",\")
            # first check amount
            if int(amount) > 1000 and trans not in ret:
                ret.append(trans)
            # second, check 60 min of another in same city
            for i in range(i+1, leng):
                if int(sorted_trans[i].split(\",\")[1]) - int(time) <= 60:
                    if sorted_trans[i].split(\",\")[3] != city and sorted_trans[i].split(\",\")[0] == name:
                        if trans not in ret: ret.append(trans)
                        if sorted_trans[i] not in ret: ret.append(sorted_trans[i])
                    continue
                else:
                    break
        return ret
