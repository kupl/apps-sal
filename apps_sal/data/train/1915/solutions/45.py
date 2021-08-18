class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        s_l, t_l = len(stamp), len(target)
        t = list(target)
        res = list()

        def stmp(i):
            match = False
            for j in range(s_l):
                if t[i + j] == '?':
                    continue
                elif t[i + j] != stamp[j]:
                    return False
                match = True
            if match:
                t[i: i + s_l] = ['?'] * s_l
                res.append(i)
            return match

        match = True
        while match:
            match = False
            for i in range(t_l - s_l + 1):
                match |= stmp(i)

        return res[::-1] if t == ['?'] * t_l else list()
