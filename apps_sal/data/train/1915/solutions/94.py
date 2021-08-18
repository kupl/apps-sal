class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n_s, n_t = len(stamp), len(target)
        stamp, target = list(stamp), list(target)

        def check(idx):
            match = False
            for i in range(n_s):
                if target[idx + i] == '?':
                    continue
                if target[idx + i] != stamp[i]:
                    return False
                match = True
            if match:
                target[idx:idx + n_s] = ['?'] * n_s
                res.append(idx)
            return match

        changed = True
        res = []
        while changed:
            changed = False
            for idx in range(n_t - n_s + 1):
                changed = changed or check(idx)

        return res[::-1] if target == ['?'] * n_t else []
