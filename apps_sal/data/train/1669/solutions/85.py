class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        card_dict = dict()
        for card in hand:
            if card in card_dict:
                card_dict[card] = card_dict[card] + 1

            else:
                card_dict[card] = 1

        while(len(card_dict) > 0):
            min_ele = min(card_dict.keys())
            for i in range(W):
                if not min_ele in card_dict:
                    return False

                elif card_dict[min_ele] > 1:
                    card_dict[min_ele] = card_dict[min_ele] - 1

                else:
                    del card_dict[min_ele]

                min_ele = min_ele + 1

        return True
