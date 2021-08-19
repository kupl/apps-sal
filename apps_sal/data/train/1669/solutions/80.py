class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand or len(hand) % W != 0:
            return False
        hand_dict = self.get_hand_dict(hand)
        return self.is_n_straigh_hand(hand_dict, W)

    def is_n_straigh_hand(self, hand_dict, W):
        while hand_dict:
            start_hand = min(hand_dict)
            for i in range(start_hand, W + start_hand):
                if i not in hand_dict:
                    return False
                else:
                    hand_dict[i] -= 1
                    if hand_dict[i] == 0:
                        del hand_dict[i]
        return True

    def get_hand_dict(self, hand):
        hand_dict = {}
        for h in hand:
            hand_dict[h] = hand_dict.get(h, 0)
            hand_dict[h] += 1
        return hand_dict
