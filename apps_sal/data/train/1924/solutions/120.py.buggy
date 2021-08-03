class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        
        stock = {}
        for trans in transactions:
            name, time, amount, city = trans.split(\",\")
            time = int(time)
            flg = False
            if int(amount)>=1000:
                flg = True
            if name in stock:
                for btime, bcity, btrans in stock[name]:
                    if (btime+60>=time and time>=btime-60)and bcity!=city:
                        if btrans not in result:
                            result.append(btrans)
                        flg = True
            if flg:
                result.append(trans)
                
            if name not in stock:
                stock[name] = [(time, city, trans)]
            else:
                stock[name].append((time, city, trans))
        return result
