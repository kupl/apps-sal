class Solution:    
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = {}
        answer = []
        for i in range(len(transactions)):
            trans = transactions[i].split(\",\")
            name,time,amt,city,ind = trans[0],int(trans[1]),int(trans[2]),trans[3],i
            
            if amt > 1000:
                answer.append(transactions[i])
                
            if name not in d:
                d[name] = [[name,time,amt,city,ind]]
            elif name in d:
                d[name].append([name,time,amt,city,ind])

        for k,v in d.items():
            v = sorted(v,key = lambda x: x[1])
            for i in range(len(v)):
                for j in range(len(v[i+1:])):
                    if (abs(v[i][1] - v[i+1:][j][1]) <= 60) and (v[i][3] != v[i+1:][j][3]):
                        if transactions[v[i][4]] not in answer:
                            answer.append(transactions[v[i][4]])
                        if transactions[v[i+1:][j][4]] not in answer:
                            answer.append(transactions[v[i+1:][j][4]])
                            
        return answer
