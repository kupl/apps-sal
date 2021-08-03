class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalids = []
        val_dict = defaultdict(list)
        
        for trs in transactions:
            #print(val_dict)
            trs_list = trs.split(\",\")
            amount = int(trs_list[2])
            
            val_dict[trs_list[0]].append((int(trs_list[1]),int(trs_list[2]), trs_list[3]))

            for trans in val_dict[trs_list[0]]:
                if abs(int(trs_list[1]) - int(trans[0])) <= 60 and trs_list[3] != trans[2]:
                    if trs not in invalids:
                        invalids.append(trs)

                    if str(trs_list[0])+\",\"+str(trans[0])+\",\"+str(trans[1])+\",\"+str(trans[2]) not in invalids:
                        invalids.append(str(trs_list[0])+\",\"+str(trans[0])+\",\"+str(trans[1])+\",\"+str(trans[2]))
                
            
            if amount > 1000:
                invalids.append(trs)
                
                
        return list(set(invalids))
                
            
            
