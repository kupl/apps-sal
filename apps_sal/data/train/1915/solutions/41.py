class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        res = []
        seq = list(target)
        m, n = len(stamp), len(target)

        def check(i):
            changed = False
            full = True
            for j in range(m):
                if seq[i + j] == '?':
                    continue
                else:
                    if target[i + j] == stamp[j]:
                        changed = True
                    else:
                        full = False
            if changed and full:
                seq[i:i + m] = ['?'] * m
                return True
            return False

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                if check(i):
                    res.append(i)
                    changed = True
        return res[::-1] if all([c == '?' for c in seq]) else []
