class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        past_ts = {}
        for t in transactions:
            vals = t.split(\",\")
            name = vals[0]
            time = int(vals[1])
            amount = int(vals[2])
            city = vals[3]
            
            if name in past_ts:
                pre_trs = past_ts[name]
                for pre_r in pre_trs:
                    pre_t = pre_r.split(\",\")
                    pre_time = int(pre_t[1])
                    pre_city = pre_t[3]
                    if abs(time - pre_time) <= 60 and city != pre_city:
                        res.add(t)
                        res.add(pre_r)
            else:
                past_ts[name] = []
            if amount > 1000:
                if t not in res:
                    res.add(t)
                    
            past_ts[name].append(t)
        return res
