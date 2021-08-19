import collections


class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        mapNameToTrans = collections.defaultdict(list)
        for t in transactions:
            (name, time, amount, city) = t.split(',')
            if int(amount) > 1000:
                invalid.append(t)
                did_add = True
            else:
                did_add = False
            for past in mapNameToTrans[name]:
                if abs(int(past[0]) - int(time)) <= 60 and past[1] != city:
                    if not did_add:
                        invalid.append(t)
                        did_add = True
                    if not past[2]:
                        past[2] = True
                        invalid.append(past[3])
            mapNameToTrans[name].append([time, city, did_add, t])
        return invalid
