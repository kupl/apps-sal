class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tr = {}
        invalids = set()
        for t in transactions:
            tl = t.split(',')
            if tl[0] not in tr:
                tr[tl[0]] = [t]
                if int(tl[2]) > 1000:
                    invalids.add(t)
            else:
                if int(tl[2]) > 1000:
                    invalids.add(t)
                tmp = tr[tl[0]]
                for temp in tmp:
                    tempo = temp.split(',')
                    if tempo[3] != tl[3]:
                        if abs(int(tempo[1]) - int(tl[1])) <= 60:
                            invalids.add(t)
                            invalids.add(temp)
                tr[tl[0]].append(t)
        return invalids
