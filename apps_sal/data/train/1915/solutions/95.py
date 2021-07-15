class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # work backward; time O(n(n-m)); space O(1)
        n_s, n_t = len(stamp), len(target)
        stamp, target = list(stamp), list(target)
        
        def check(idx):
            match = False
            for j in range(n_s):
                if target[idx+j] == '?': 
                    continue
                if target[idx+j] != stamp[j]:
                    return False
                match = True
            if match:
                target[idx:idx+n_s] = ['?'] * n_s
                res.append(idx)
            return match
        
        changed = True
        res = []
        while changed:
            changed = False
            for idx in range(n_t - n_s + 1):
                changed = changed or check(idx)
        
        return res[::-1] if target == ['?'] * n_t else []
