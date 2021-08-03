class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = defaultdict(list)
        res = []
        def helper(s):
            sl = s.split(\",\")
            name = sl[0]
            time = sl[1]
            amount = sl[2]
            city = sl[3]
            return name,time,amount,city
        
        for i in transactions:
            name,time,amount,city = helper(i)
            
            if int(amount) > 1000:
                res.append(i)
                
            for j in dic[name]:
                if abs(int(j[0])-int(time))<=60 and j[2] != city:
                    if name+','+\",\".join(j) not in res:
                        res.append(name+','+\",\".join(j))
                    if i not in res:
                        res.append(i)
                
            dic[name].append([time,amount,city])
            
        return res
