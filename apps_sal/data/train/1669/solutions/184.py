class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        count = collections.Counter(hand)
        while count:
            key = list(count.keys())[0]
            for i in range(W):
                if count[key + i] > 0:
                    count[key + i] -= 1
                    if count[key + i] == 0:
                        del count[key + i]
                else:
                    return False
        return True
