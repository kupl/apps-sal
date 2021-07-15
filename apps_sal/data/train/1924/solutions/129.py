from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = defaultdict(list)
        res = set()
        for i in transactions: 
            i = i.split(',')
            if int(i[2]) > 1000:
                res.add(','.join(i))
            if i[0] in dic: #we only care about time and place
                    for j in dic[i[0]]:
                        j = j.split(',')
                        if i[3] != j[3] and abs(int(i[1]) - int(j[1])) <= 60:
                            res.add(','.join(i))
                            res.add(','.join(j))
            dic[i[0]].append(','.join(i))
        print(dic)
        return list(res)

