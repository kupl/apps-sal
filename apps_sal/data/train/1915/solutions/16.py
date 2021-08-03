class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        t = list(target)
        res = []

        def check(i):
            if t[i:i + m] == ['?'] * m:
                return False

            for j in range(m):
                if t[i + j] not in ['?', stamp[j]]:
                    return False

            t[i:i + m] = ['?'] * m
            res.append(i)
            return True

        change = True
        while change:
            change = False
            for i in range(n - m + 1):
                change |= check(i)

        return res[::-1] if t == ['?'] * n else []
