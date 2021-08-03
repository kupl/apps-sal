class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # abc??
        # ?abc?
        # ??abc

        def num_match(stamp, target):
            ret = 0
            for (c1, c2) in zip(stamp, target):
                if c1 == c2:
                    ret += 1
                elif c2 != '?':
                    return -1
            return ret

        remain = len(target)
        ret = []
        cur = list(target)
        while remain > 0:
            tmp = remain
            match = 0
            for l in range(len(target)):
                r = l + len(stamp) - 1
                if r >= len(target):
                    break
                match = num_match(stamp, cur[l:r + 1])
                if match > 0:
                    cur[l:l + len(stamp)] = ['?'] * len(stamp)
                    ret.append(l)
                    remain -= match

            if tmp == remain:
                return []

        return ret[::-1]
