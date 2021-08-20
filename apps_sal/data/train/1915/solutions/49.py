class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        def okay(s):
            ret = False
            for (c1, c2) in zip(stamp, s):
                if c2 == '?':
                    continue
                elif c1 != c2:
                    return False
                else:
                    ret = True
            return ret
        todo = len(target) - len(stamp) + 1
        res = []
        idx = 0
        while idx < todo:
            prv = idx
            for i in range(todo):
                if okay(target[i:i + len(stamp)]):
                    idx += 1
                    res.append(i)
                    target = target[:i] + '?' * len(stamp) + target[i + len(stamp):]
            if target == '?' * len(target):
                return res[::-1]
            if idx == prv:
                break
        return []
