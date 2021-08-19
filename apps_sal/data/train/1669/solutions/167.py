from collections import OrderedDict


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        card_counts = OrderedDict()

        for i in range(len(hand)):
            card_counts[hand[i]] = card_counts.get(hand[i], 0) + 1

        keys = sorted(card_counts.keys())

        while card_counts:
            min_val = keys[0]
            for hand in range(min_val, min_val + W):
                # print(hand[i])
                # print(card_counts)
                if hand not in card_counts:
                    return False

                count = card_counts[hand]
                if count == 1:
                    keys.pop(0)
                    del card_counts[hand]
                else:
                    card_counts[hand] -= 1

        return True
