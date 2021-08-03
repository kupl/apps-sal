class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        items = sorted(zip(keyTime, keyName))
        
        beg, count = 0, Counter()
        res = set()
        for t, name in items:
            p = t.split(':')
            p = (int(p[0]) - 1, p[1])
            if p[0] >= 0:
                p = \"{0:02}:{1}\".format(*p)
                while beg < len(items) and items[beg][0] < p:
                    count[items[beg][1]] -= 1
                    beg += 1
            count[name] += 1
            if count[name] >= 3:
                res.add(name)
                
        return sorted(res)
