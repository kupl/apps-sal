class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = Counter(hand)
        while c:
            x = min(c.keys())
            for i in range(x,x+W):
                if i not in c: return False
                c[i] -= 1
                if c[i] == 0: del c[i]
        return True
