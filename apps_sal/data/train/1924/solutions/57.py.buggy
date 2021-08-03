import collections

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        output = []
        trans_dict = collections.defaultdict()
        
        for t in transactions:
            name, time, amount, city = t.split(\",\")
            if float(amount) > 1000:
                output.append(t)
            
            if name not in trans_dict.keys():
                trans_dict[name] = collections.defaultdict(list)
            
            trans_dict[name][city].append((int(time), amount))
            
            for c in trans_dict[name].keys():
                # print(t, \"t1\")
                if c != city:
                    for ta in trans_dict[name][c]:
                        t2, a2 = ta
                        # print(t, \"t2\", t2, int(time), a2)
                        if abs(t2-int(time))<=60:
                            prev_trans = name+\",\"+str(t2)+\",\"+a2+\",\"+c
                            if prev_trans not in output:
                                output.append(prev_trans)
                            if t not in output:
                                output.append(t)


        return output
        
