class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp = list(stamp)
        target = list(target)
        res = []
        
        def check(i):
            changed = False
            for j in range(len(stamp)):
                if target[i+j] == '?': continue
                if target[i+j] != stamp[j]: return False
                changed = True

            return changed
            
        seen = [0] * len(target)   
        ans = True
        while ans:
            ans = False
            for i in range(len(target) - len(stamp) + 1):
                changed = check(i)               
                ans = ans or changed
                            
                if changed:
                    res.append(i)
                    target[i:i+len(stamp)] = ['?'] * len(stamp)
                    seen[i:i+len(stamp)] = [1] * len(stamp)
                               
        return res[::-1] if sum(seen) == len(target) else []

