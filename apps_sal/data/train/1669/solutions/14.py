class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W:
            return False

        C = Counter(hand)
        #print (C)
        for i in range(n // W):
            mn = min(C.keys())
            for j in range(mn, mn + W):
                if j not in C:
                    return False
                else:
                    C[j] -= 1
                    if C[j] == 0:
                        del C[j]

        return True
