class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        root = '?' * (n := len(target))
        res = []
        moves = 0

        def match(s, t):
            for (c1, c2) in zip(s, t):
                if c1 == '?':
                    continue
                elif c1 != c2:
                    return False
            return True
        while moves <= 10 * n:
            prev_move = moves
            for i in range(n - (m := len(stamp)) + 1):
                if target[i] in {stamp[0], '?'} and match(target[i:i + m], stamp):
                    moves += 1
                    res.append(i)
                    target = target[:i] + '?' * m + target[i + m:]
                    if target == root:
                        return res[::-1]
            if prev_move == moves:
                return []
        return []
