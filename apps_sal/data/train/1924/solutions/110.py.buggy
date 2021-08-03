class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        output = []
        names = {}
        inOutput = set()
        
        for idx, trans in enumerate(transactions):
            curr = trans.split(\",\")
            print(curr)
            
            if curr[0] not in names:
                names[curr[0]] = [idx]
            else:
                for transIdx in names[curr[0]]:
                    personTrans = transactions[transIdx].split(\",\")
                    if curr[3] != personTrans[3] and abs(int(curr[1]) - int(personTrans[1])) <= 60:
                        if idx not in inOutput:
                            output.append(trans)
                            inOutput.add(idx)
                        if transIdx not in inOutput:
                            output.append(transactions[transIdx])
                            inOutput.add(transIdx)
                names[curr[0]].append(idx)
                
            if int(curr[2]) > 1000 and idx not in inOutput:
                output.append(trans)
                inOutput.add(idx)
        
        return output
