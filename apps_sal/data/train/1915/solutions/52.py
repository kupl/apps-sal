class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        root = '?' * (n := len(target))
        res = []
        moves = 0

        def match(s, t):
            for (ch1, ch2) in zip(s, t):
                if ch1 == '?':
                    continue
                elif ch1 != ch2:
                    return False
            return True
        while moves <= 10 * n:
            pre_move = 0
            for i in range(n - (m := len(stamp)) + 1):
                if target[i] in {stamp[0], '?'} and match(target[i:i + m], stamp):
                    moves += 1
                    res.append(i)
                    target = target[:i] + '?' * m + target[i + m:]
                    if target == root:
                        return reversed(res)
            if pre_move == moves:
                return []
        return []
