class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        done = set()
        n = len(stamp)
        m = len(target)
        candidates = { i for i in range(m-n+1) }
        res = []
        
        def check(i):
            j = 0
            count = 0
            while j < n :
                if i in done:
                    j += 1
                    i += 1
                elif stamp[j] == target[i]:
                    count += 1
                    i += 1
                    j += 1
                else:
                    return -1
            if count == 0:
                return 0
            else:
                return 1
        
        while len(done) < m :
            found = 0
            remove = set()
            for i in candidates:
                I = check(i)
                if I == 1:
                    for j in range(i,i+n):
                        done.add(j)
                    res.append(i)
                    found = 1
                    break
                elif I == 0:
                    remove.add(i)
                    
            if not found:
                return []
            else:
                candidates.remove(i)
                candidates -= remove
                
                    
        return res[::-1]
                
            
        
        

