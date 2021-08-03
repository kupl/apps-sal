class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        def formated(ob):
            return ob['name']+\",\"+str(ob['time'])+\",\"+str(ob['amount'])+\",\"+ob['city']
        l=[]
        res=[]
        for i in range(len(transactions)):
            store=dict()
            n,t,amount,city = transactions[i].split(\",\")
            store['name']=n
            store['time']=int(t)
            store['amount']=int(amount)
            store['city']=city
            l.append(store)

        sortedList= sorted(l, key = lambda i: i['time'])
        
        for i in range(len(sortedList)):
            for j in range(len(sortedList)):
                if i==j:
                    continue
                    
                elif sortedList[i]['name']==sortedList[j]['name'] and abs(sortedList[i]['time'] - sortedList[j]['time'])<=60 and sortedList[i]['city']!=sortedList[j]['city']:
                    res.append(formated(sortedList[i]))
                    break

                elif sortedList[i]['amount']>1000:
                    res.append(formated(sortedList[i]))
                    break
                    
                elif sortedList[j]['time'] - sortedList[i]['time']>60:
                    break
                    
        return res
        
