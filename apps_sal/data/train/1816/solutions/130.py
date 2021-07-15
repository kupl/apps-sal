class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mp = collections.defaultdict(list)
        
        for n, t in sorted(zip(keyName, keyTime)):
            minutes = int(t[:2]) * 60 + int(t[3:])
            mp[n].append(minutes)
        
        ret = []
        
        for n, t in list(mp.items()):
            if len(t) < 2:
                continue
            
            i = 0
            
            for j, val in enumerate(t):
                while val - t[i] > 60:
                    i += 1
                
                if j - i >= 2:
                    ret.append(n)
                    break
        
        return ret
            

