class T:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    def get_string(self):
        return self.name+\",\"+str(self.time)+\",\"+str(self.amount)+\",\"+self.city

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # create T object
        ts = []
        for tran in transactions:
            ts.append(T(*tran.split(\",\")))
        ts.sort(key=lambda t: t.time)
        name2t = defaultdict(list)
        
        for t in ts:
            name2t[t.name].append(t)
        res = []
        for name,ts in name2t.items():
            for i,t in enumerate(ts):
                left,right = 0,0
                if t.amount > 1000: 
                    res.append(t.get_string())
                    continue
                
                while left <= len(ts)-2 and ts[left].time < t.time-60: # O(60)
                    left+=1 # 아주맨마지막까지가는거 가능
                while right <= len(ts)-2 and ts[right+1].time <= t.time+60: # O(60)
                    right+=1 # 아주맨마지막까지가는거 가능
                    
                for i in range(left, right+1): # O(120)
                    cand_t = ts[i]
                    if cand_t.city != t.city:
                        res.append(t.get_string())
                        break
        return res
