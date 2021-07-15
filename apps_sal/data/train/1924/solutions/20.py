class Solution:
    
    def invalidTransactions(self, transactions):
        if not transactions: return []
        n = len(transactions)
        splits = [trans.split(',') for trans in transactions]
        valid = [True] * n

        for i in range(n):   #   rule 1
            if int(splits[i][2]) > 1000:
                valid[i] = False

        for i in range(n):       #   rule 2
            for j in range(i+1, n):                
                if valid[i] or valid[j]:
                    name1, time1, city1 = splits[i][0], int(splits[i][1]), splits[i][3]
                    name2, time2, city2 = splits[j][0], int(splits[j][1]), splits[j][3]
                    if name1 == name2 and city1 != city2 and abs(time1-time2)<=60:
                        valid[i], valid[j] = False, False

        return [transactions[i] for i in range(n) if not valid[i]]
    
#     def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
# #         def asPerTime(string):
# #             return string.split(',')[1]
            
        
# #         transactions.sort(key=asPerTime)
        
#         #dictionary
#         personDict = dict()
        
#         #outputList
#         outSet = set()
        
#         for transaction in transactions:
#             name, time, amount, city = transaction.split(',')
#             if int(amount) > 1000:
#                 outSet.add(transaction)
                
#             if name in personDict:
#                 cityDict = personDict[name]
#                 cityDict[city].append((time, amount))
                
#                 for key in cityDict:
#                     if key != city:
#                         for pair in cityDict[key]:
#                             prevTime, prevAmount = pair
#                             timeDiff = abs(int(time) - int(prevTime)) 
#                             if timeDiff <= 60:
#                                 outSet.add(transaction)
#                                 outSet.add(','.join([name, prevTime, prevAmount, key]))
            
            
#             else:
#                 personDict[name] = defaultdict(list)
#                 personDict[name][city].append((time, amount)) 
        
        
#         return outSet
        
        
        '''
        sort the transaction list as per the time
        
        a dictionary where key is the name of the person and the the value is a dictionary where the key is the city and the value is time and amount        
        
        
        
        iterate over the transactions:
            if the amount is greater than 1000:
                add it to the list
            
            if that same person has done a transaction before
                are the cities different:
                    get the time of the latest transaction
                    if difference is <60:
                        add the latest transaction as well as this transaction
                        update the latest transaction with this transaction info
                        continue
                        
                 
        '''
        
        

