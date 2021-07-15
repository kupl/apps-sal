class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = defaultdict(list)
        ans = set()
        for trans in transactions:
            name, time, amt, loc = trans.split(',')
            if int(amt) > 1000:
                ans.add(trans)
            for trans2 in dic[name]:
                other = trans2.split(',')
                if other[3] != loc and abs(int(other[1]) - int(time)) <= 60:
                    ans.add(trans)
                    ans.add(trans2)
            dic[name].append(trans)
        
        return ans
