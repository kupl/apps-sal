class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # time order?
        # 30 60 90 how to assess?
        
        realTransactions = collections.defaultdict(list)
        for each in transactions:
            each = each.split(',')
            realTransactions[each[0]].append(tuple(each[1:]))
        
        res = []
        for name in realTransactions.keys(): # O(n) time
            realTransactions[name].sort(key = lambda x: int(x[0]))
            for i, trans in enumerate(realTransactions[name]):
                left = right = i
                time, amt, loc = trans
                if int(amt) > 1000:
                    res.append(\"{},{},{},{}\".format(name, time, amt, loc))
                    continue
                while left - 1 >= 0 and int(realTransactions[name][left - 1][0]) + 60 >= int(time):
                    left -= 1
                while right + 1 < len(realTransactions[name]) and int(realTransactions[name][right + 1][0]) - 60 <= int(time):
                    right += 1
                #print(left, right)
                for idx in range(left, right + 1):
                    if realTransactions[name][idx][2] != loc:
                        res.append(\"{},{},{},{}\".format(name, realTransactions[name][i][0], realTransactions[name][i][1], realTransactions[name][i][2]))
                        break

        return res
            
