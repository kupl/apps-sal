class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ret = set()
        name = []
        time = []
        amount = []
        city = []
        for trans in transactions:
            trans = trans.split(',')
            name.append(trans[0])
            time.append(int(trans[1]))
            amount.append(int(trans[2]))
            city.append(trans[3])
        for i in range(len(transactions)):
            if amount[i] > 1000:
                ret.add(transactions[i])
            for j in range(i + 1, len(transactions)):
                if name[i] == name[j] and abs(time[i] - time[j]) <= 60 and (city[i] != city[j]):
                    ret.add(transactions[i])
                    ret.add(transactions[j])
        return ret
