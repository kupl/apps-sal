class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False

        counts = collections.Counter(hand)

        while sum(counts.values()) > 0:
            start_card = min(counts)
            print(start_card)

            for card in range(start_card, start_card + W):
                if card not in counts:
                    return False
                counts[card] -= 1
                if counts[card] == 0:
                    del counts[card]

        return True
