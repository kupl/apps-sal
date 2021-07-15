class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        track = [] # (time, city, name)
        ret = set()
        
        for t in transactions:
            name, time, amt, city = t.split(\",\")
            time = int(time)
            if int(amt) > 1000:
                ret.add(t)
                track.append((time, city, name, t))

            # print(track, t)
            for i in range(0, len(track)):
                cmp = track[i]
                if abs(cmp[0] - time) <= 60 and cmp[1] != city and cmp[2] == name:
                    ret.add(t)
                    ret.add(cmp[3])
            
            track.append((time, city, name, t))
        return ret
