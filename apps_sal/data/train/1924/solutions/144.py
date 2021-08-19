class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        dic = defaultdict(list)
        invalid = set()
        for i in range(len(transactions)):
            name, time, amount, city = (int(i) if i.isnumeric() else i for i in transactions[i].split(','))
            if amount > 1000:
                invalid.add(transactions[i])
            if name in dic:
                for tran in dic[name]:
                    _, prev_time, _, prev_city = (int(i) if i.isnumeric() else i for i in tran.split(','))
                    if prev_city != city and abs(prev_time - time) <= 60:
                        invalid.add(tran)
                        invalid.add(transactions[i])
            dic[name].append(transactions[i])
        return list(invalid)


#         import collections
#         if not transactions:
#             return []

#         memo = collections.defaultdict(list)    #create a dictionary to keep track of previous transaction
#         invalid_tran = set()                    #to store invalid transaction / I use set to avoid duplication
#         for i in range(len(transactions)):

#             name, time, amount, city = (int(i) if i.isnumeric() else i for i in transactions[i].split(','))

#             if amount > 1000:                   #if the amount is greater than 1000 add it to the invalid_tran
#                 invalid_tran.add(transactions[i])

#             if name in memo:                    # if there is any other previous transaction done by similar person , check it from the memo
#                 for tran in memo[name]:         # bring all previous transaction done by similar person (iterate over the memo)
#                     _, prev_time, _, prev_city =(int(i) if i.isnumeric() else i for i in  tran.split(','))
#                     if abs(time-prev_time) <= 60 and prev_city != city:  #check if the absolute time difference is less than 60 and the city is the same
#                         invalid_tran.add(tran)
#                         invalid_tran.add(transactions[i])

#             memo[name].append(transactions[i])  # add the transaction to the dictionary (memo) - always keep track of previous transaction
#         return invalid_tran
