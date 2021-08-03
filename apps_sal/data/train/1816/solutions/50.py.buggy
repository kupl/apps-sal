import heapq
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = {}
        aler = set()
        
        for (name,time) in sorted(zip(keyName,keyTime) , key = lambda x: x[1]):
            if name in aler:
                continue
                
            h,m = time.split(\":\")
            stamp = (int(h)*60 + int(m))%(24*60)
            #print(h,m)
            
            if name not in d: 
                d[name] = [stamp]
                heapq.heapify(d[name])
            else:
                heapq.heappush(d[name],stamp)
                if stamp <= d[name][0] + 60:
                    if len(d[name]) >= 3:
                        aler.add(name)
                        del d[name]
                else:
                    while d[name] and d[name][0]+60 < stamp:
                        del d[name][0]
                    
            #print(d)
        return sorted(aler)
                
                
