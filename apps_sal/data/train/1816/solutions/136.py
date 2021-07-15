class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        pl = sorted(zip(keyName, keyTime))
        d = collections.defaultdict(list)
        r = []
        def isIn1(t1, t2):
            h1, m1 = t1.split(\":\")
            h2, m2 = t2.split(\":\")
            if h1 == h2 or (int(h2) - int(h1) == 1 and int(m2)-int(m1) <= 0):
                return 1
            return 0
        
        for n, t in pl:
            if r and r[-1] == n: continue
            pt = d[n]
            if len(pt) >= 2:
                if isIn1(pt[-2], t):
                    r.append(n)
            d[n].append(t)
        
        return r
