class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0 or not W:
            return False

        avail = collections.Counter(hand)
        while avail:
            curr = min(avail)
            for i in range(W):
                if avail[curr + i]:
                    avail[curr + i] -= 1
                    if not avail[curr + i]:
                        del avail[curr + i]
                else:
                    return False
        return True
