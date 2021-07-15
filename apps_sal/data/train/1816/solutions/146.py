class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        doc = collections.defaultdict(collections.deque)
        res = set()
        
        for name, time in sorted(zip(keyName, keyTime), key=lambda x: x[1]):
            while doc[name] and self.delta_time(time, doc[name][0]) > 60:
                doc[name].popleft()

            doc[name].append(time)
            if len(doc[name]) >= 3:
                res.add(name)
        return sorted(list(res))
    
    def delta_time(self, t1, t2):
        h1, m1 = t1.split(':')
        h2, m2 = t2.split(':')
        return int(h1) * 60 + int(m1) - (int(h2) * 60 + int(m2))

