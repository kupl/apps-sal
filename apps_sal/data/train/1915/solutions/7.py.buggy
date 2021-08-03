# ababcbc
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        s, t = list(stamp), list(target)
        ans = []
        
        def check(idx):
            changed = False
            for i in range(m):
                if t[idx + i] == \"?\": continue
                if t[idx + i] != s[i]: return False
                changed = True
            if changed:
                t[idx: idx + m] = [\"?\"] * m
                ans.append(idx)
            return changed
            
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                if check(i):
                    changed = True
                    break
        return ans[::-1] if t == [\"?\"] * n else []
                
