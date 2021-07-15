class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        M, N = len(stamp), len(target)
        stamp, target = list(stamp), list(target)
        
        ans = []
        
        def check(i):
            needsUpdate = False
            for j in range(M):
                if target[i+j] == '?':
                    continue
                if target[i+j] != stamp[j]:
                    return False
                needsUpdate = True
            
            if needsUpdate:
                target[i:i+M] = '?' * M
                ans.append(i)
            return needsUpdate
            
        
        changed = True
        while changed:
            changed = False
            for i in range(N - M + 1):
                if check(i):
                    changed = True
                    break

        return ans[::-1] if target.count('?') == len(target) else []
        

