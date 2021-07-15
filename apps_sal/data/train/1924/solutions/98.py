class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        mp = {}
        res = set()
        for string in transactions:
            l = string.split(',')
            person = l[0]
            time = l[1]
            amount = l[2]
            city = l[3]
            
            if int(amount)>1000:
                res.add(string)
                #continue
                
            if person in mp:
                #print(mp[person])
                for val in mp[person]:
                    time_1 = val[0]
                    if abs(int(time)-int(time_1))<=60 and val[2]!=city:
                        print(abs(int(time)-int(time_1)))
                        str1 = person+\",\"+time_1+\",\"+val[1]+\",\"+val[2]
                        res.add(str1)
                        res.add(string)
            if person not in mp:
                mp[person] = [[time,amount,city]]
            else:
                mp[person].append([time,amount,city])
            
        
        r = [x for x in res]
        return r
