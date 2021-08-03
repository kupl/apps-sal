class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        seen = {}
        for i in range(len(transactions)):
            trans = transactions[i].split(\",\")
            if trans[0] in seen: 
                for old in seen[trans[0]]:
                    if old[0] != trans[3] and abs(int(old[1])-int(trans[1])) <= 60:
                        invalid.add(transactions[i])
                        invalid.add(transactions[old[2]])
            if int(trans[2]) > 1000:
                invalid.add(transactions[i])
            
            if trans[0] in seen:
                seen[trans[0]].append([trans[3],trans[1],i])
            else:
                seen[trans[0]] = [[trans[3],trans[1],i]]
        
        return invalid
            
            
