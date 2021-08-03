class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        arr = list(zip(keyTime, keyName))
        arr.sort()
        
        self.d = collections.defaultdict(collections.deque)
        res = set()
        
        for t, name in arr:
            h, m = t.split(\":\")
            minutes = int(h) * 60 + int(m)
            
            while self.d[name] and minutes - self.d[name][0] > 60:
                self.d[name].popleft()
            
            self.d[name].append(minutes)
            
            if len(self.d[name]) >= 3:
                res.add(name)
        
        return(sorted(list(res)))
