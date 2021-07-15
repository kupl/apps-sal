class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        cardCount = {}

        for card in hand:
            if not card in cardCount:
                cardCount[card] = 0
            cardCount[card] += 1

        k = len(hand) // W

        for i in range(k):
            start = min(cardCount.keys())
            
            for j in range(W):
                if not start + j in cardCount:
                    return False

            for j in range(W):
                cardCount[start + j] -= 1
                if cardCount[start + j] == 0:
                    cardCount.pop(start + j)

        return True


