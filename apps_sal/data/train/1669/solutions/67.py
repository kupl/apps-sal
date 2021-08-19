class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False

        hand = sorted(hand)
        counts = collections.Counter(hand)  # key: card, val: freq
        print(counts)
        # tree map: ordered hashmap
        while sum(counts.values()) > 0:
            start_card = min(counts)
            print(start_card)

            for card in range(start_card, start_card + W):
                # check each group in one for-loop
                if card not in counts:
                    return False
                counts[card] -= 1
                if counts[card] == 0:
                    del counts[card]

            # counts[start_card] -= 1
            # if counts[start_card] == 0:
            #     del counts[start_card]

        return True
