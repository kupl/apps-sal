class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        count = Counter(hand)
        for i in range(len(hand) // W):
            num = min(count.keys())
            for j in range(W):
                count[num + j] -= 1
                if count[num + j] == 0:
                    del count[num + j]
                elif count[num + j] < 0:
                    return False
        return True
