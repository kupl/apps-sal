class Solution:

    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        def giddy(item):
            return item.split(',')
        result = set()
        seen = collections.defaultdict(list)
        transactions = list(map(giddy, transactions))
        for i in range(len(transactions)):
            val = transactions[i]
            if int(val[2]) > 1000:
                result.add(','.join(val))
            if val[0] in seen:
                for x in seen[val[0]]:
                    comp = transactions[x]
                    if abs(int(comp[1]) - int(val[1])) <= 60 and comp[3] != val[3]:
                        result.add(','.join(val))
                        result.add(','.join(comp))
            seen[val[0]].append(i)
        return result
