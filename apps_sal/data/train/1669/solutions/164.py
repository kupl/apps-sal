class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand:
            return W == 0
        if len(hand) % W != 0:
            return False
        hand.sort()

        def isnstraighthand(li):
            if not li:
                return True
            start = li[0]
            for i in range(start, start + W):
                if i not in li:
                    return False
                else:
                    li.remove(i)
            return isnstraighthand(li)

        return isnstraighthand(hand)
