class Solution:
    def invalidTransactions(self, arr: List[str]) -> List[str]:
        self.memo = collections.defaultdict(list)
        ans = set()
        for s in arr:
            name, mi, mon, place = s.split(\",\")
            if int(mon) > 1000:
                ans.add(s)
            if self.memo[name]:
                flag = False
                for a,b,c,d in self.memo[name]:
                    if d != place and abs(int(mi) - b) <= 60:
                        flag = True
                        ans.add(a + \",\" + str(b) + \",\" + str(c) + \",\" + d)
                if flag:
                    ans.add(s)
            self.memo[name] += ((name, int(mi), int(mon), place)),
        return ans

