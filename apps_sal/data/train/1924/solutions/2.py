class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        record, res = collections.defaultdict(list), set()
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            amount, time = int(amount), int(time)
            if amount > 1000:
                res.add(trans)
            if name in record:
                i, j = bisect.bisect_left(record[name], (time - 60, '', 0)), bisect.bisect_right(record[name], (time + 61, '', 0))
                valid = True
                for item in record[name][i:j]:
                    if item[1] != city:
                        valid = False
                        res.add(','.join([name, str(item[0]), str(item[2]), item[1]]))
                if not valid:
                    res.add(trans)
            bisect.insort(record[name], (time, city, amount))
        return list(res)
