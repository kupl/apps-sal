class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        poss = []
        people = {}
        for t in transactions:
            items = t.split(\",\")
            if int(items[2]) > 1000:
                poss.append(t)
           
            if items[0] in people:
                for a,b, c in people[items[0]]:
                    if abs(a - int(items[1])) <= 60 and items[3] != b:
                        if t not in poss: 
                            poss.append(t)
                        if c not in poss: 
                            poss.append(c) 
                people[items[0]].append((int(items[1]), items[3], t))
            else:
                people[items[0]] = [(int(items[1]), items[3], t)]
        return poss
