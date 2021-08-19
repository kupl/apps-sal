class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        (ls, lt) = (list(stamp), list(target))
        (m, n) = (len(ls), len(lt))
        (todo, move, res) = (n - m + 1, 0, [])

        def match(lst, ls):
            ret = False
            for (c1, c2) in zip(lst, ls):
                if c1 == '?':
                    continue
                elif c1 != c2:
                    return False
                else:
                    ret = True
            if ret:
                lt[i:i + m] = ['?'] * m
            return ret
        while move < todo:
            prv = move
            for i in range(n - m + 1):
                if match(lt[i:i + m], ls):
                    move += 1
                    res.append(i)
            if lt == ['?'] * n:
                return res[::-1]
            if prv == move:
                break
        return []
