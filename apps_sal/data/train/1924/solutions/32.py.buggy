class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans_map, suspect = {}, []
        
        for trans in transactions:
            name, time, amount, city = trans.split(\",\")
            
            if name not in trans_map.keys():
                trans_map[name] = [(int(time), int(amount), city, trans)]
            else:
                for prev in trans_map[name]:
                    oth_time, oth_amount, oth_city, oth_trans = prev
                
                    if city != oth_city and abs(int(time) - oth_time) <= 60:
                        if trans not in suspect:
                            suspect.append(trans)
                        
                        if oth_trans not in suspect:
                            suspect.append(oth_trans)
                        
                trans_map[name].append((int(time), int(amount), city, trans))
                    
            if int(amount) > 1000:
                if trans not in suspect:
                    suspect.append(trans)
                
        
        return suspect
            
            
                
        
