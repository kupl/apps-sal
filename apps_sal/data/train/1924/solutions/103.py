import collections


class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        mapNameToTrans = collections.defaultdict(list)
        for t in transactions:
            (name, time, amount, city) = t.split(',')
            did_add = False
            if int(amount) > 1000:
                invalid.append(t)
                did_add = True
            for past in mapNameToTrans[name]:
                (past_name, past_time, past_amount, past_city) = past[0].split(',')
                if past_city != city and abs(int(past_time) - int(time)) <= 60:
                    if not did_add:
                        invalid.append(t)
                        did_add = True
                    if not past[1]:
                        past[1] = True
                        invalid.append(past[0])
            mapNameToTrans[name].append([t, did_add])
        return invalid
