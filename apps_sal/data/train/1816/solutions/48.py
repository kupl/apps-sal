class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        used = {}
        res = set()
        
        def greaterThanHour(t1, t2):
            t1 = t1.split(':')
            t2 = t2.split(':')
            h1, h2 = int(t1[0]), int(t2[0])  
            m1, m2 = int(t1[1]), int(t2[1])
                
            return ((h2-h1)*60 + (m2 - m1)) > 60
        
        for n, t in zip(keyName, keyTime):
            if n not in used:
                used[n] = []
            
            used[n].append(t)

        for k in used:
            used[k] = sorted(used[k])
            p1 = p2 = 0
            
            while p2 < len(used[k]):
                if greaterThanHour(used[k][p1], used[k][p2]):
                    p1 += 1
                if p2 - p1 == 2:
                    res.add(k)
                    break
                p2 += 1

        return sorted(list(res))
