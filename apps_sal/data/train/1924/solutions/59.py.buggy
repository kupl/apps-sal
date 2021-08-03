class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        inv = set()
        
        for i in range(len(transactions)):
            cur = transactions[i].split(\",\")
            if (int(cur[2]) > 1000):
                inv.add(','.join(cur))
                cur_inv = True
            for j in range(i, len(transactions) - 1):
                comp = transactions[j + 1].split(\",\")
                if (comp[0] == cur[0]):
                    if (abs(int(comp[1]) - int(cur[1])) <= 60 and comp[3] != cur[3]):
                        inv.add(','.join(cur))
                        inv.add(','.join(comp))
        return inv
