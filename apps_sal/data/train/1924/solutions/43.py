class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        records = []
        
        for t in transactions:
            rec = t.split(',')
            rec[1] = int(rec[1])
            rec[2] = int(rec[2])
            records.append(rec)
        for rec in records:
            if rec[2] > 1000:
                rec[1] = str(rec[1])
                rec[2] = str(rec[2])
                res.append(','.join(rec))
                continue
            for x in records:
                if rec[0] == x[0] and abs(rec[1] - int(x[1])) <=60 and rec[3] != x[3]:
                    rec[1] = str(rec[1])
                    rec[2] = str(rec[2])
                    res.append(','.join(rec))
                    break
        return res
