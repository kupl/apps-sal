class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        from collections import deque
        inp = defaultdict(list)
        for k, v in zip(keyName, keyTime):
            inp[k].append(v)
        out = []
        for k,v in inp.items():
            n = sorted(v)
            time = deque()
            for i in n:
                tmp = i.split(\":\")
                time.append((int(tmp[0])*60)+int(tmp[1]))
                for j in list(time):
                    if abs(time[-1]-j)>60:
                        time.popleft()
                if len(list(time))>=3:
                    out.append(k)
                    
        return sorted(set(out))
            
                    
                
            
        
    
