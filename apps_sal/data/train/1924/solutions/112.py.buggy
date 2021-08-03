class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        trans_list = [[x for x in trans.split(\",\")] for trans in transactions]
        transactions_by_name = collections.defaultdict(list)
        for x in trans_list:
            transactions_by_name[x[0]].append(x[1:])
        res = []
        for name, values_list in transactions_by_name.items():
            for values in values_list:
                time, amount, city = values
                if int(amount) > 1000:
                    res.append(','.join([name, time, amount, city]))
                else:
                    for other_values in values_list:
                        otime, _, ocity = other_values
                        if ocity != city and abs(int(time) - int(otime)) <= 60:
                            res.append(','.join([name, time, amount, city]))
                            break
        return res
                
