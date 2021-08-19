class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W:
            return False
        C = Counter(hand)
        keys = sorted(C.keys())
        for i in range(n // W):
            mn = keys[0]
            for j in range(mn, mn + W):
                if j not in keys:
                    return False
                else:
                    C[j] -= 1
                    if C[j] == 0:
                        del C[j]
                        keys.remove(j)
        return True
