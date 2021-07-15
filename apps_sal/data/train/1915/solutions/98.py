class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s,t = list(stamp),list(target)
        n,m = len(s),len(t)
        res = []
        def check(i):
            changed = False
            for j in range(n):
                if t[i+j] == '?':continue
                if t[i+j] != s[j]:return False
                else:
                    changed = True
            if changed:
                t[i:i+n] = ['?']*n
                res.append(i)
            return changed
        chan = True
        while chan:
            chan = False
            for i in range(m-n+1):
                chan = chan or check(i)
        return res[::-1] if t == ['?']*m else []
