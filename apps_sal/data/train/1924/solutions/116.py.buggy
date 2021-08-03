class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         transaction invalid -> > $1000 or within 60 minutes and same name and diff city
        
#         loop thru the list 
#         for each item, split the string by comma
#         set dictionary with name for key
#         list of tuple for value with time, cost, location
        
#         loop thru dictionary
#         sort the list by time / 0 index 
            
        clean = {}
        results = set()
        
        for transaction in transactions:
            item = transaction.split(',')
            name, time, money, location = item
            if name not in clean:
                clean[name] = [(int(time), int(money), location)]
            else:
                clean[name].append((int(time), int(money), location))
        
        for person, info in clean.items():
            sorted_items = sorted(info)
            for idx in range(len(sorted_items)):
                for idx_2 in range(len(sorted_items)):
                    if (abs(sorted_items[idx_2][0] - sorted_items[idx][0]) <= 60) and (sorted_items[idx_2][2] != sorted_items[idx][2]) and (idx != idx_2): 
                        invalid_1 = [person, str(sorted_items[idx][0]), str(sorted_items[idx][1]), sorted_items[idx][2]]
                        invalid_2 = [person, str(sorted_items[idx_2][0]), str(sorted_items[idx_2][1]), sorted_items[idx_2][2]]
                        results.add(\",\".join(invalid_1))
                        results.add(\",\".join(invalid_2))
                
                cost = sorted_items[idx][1]
                if cost > 1000:
                    invalid = [person, str(sorted_items[idx][0]), str(sorted_items[idx][1]), sorted_items[idx][2]]
                    results.add(\",\".join(invalid))
        
        return list(results)
        
