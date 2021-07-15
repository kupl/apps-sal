class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count_map = Counter()
        for num in hand:
            count_map[num] += 1
        test = sorted(count_map)
        sorted_hand = sorted(dict.fromkeys(hand))
        while len(sorted_hand) > 0:
            while len(sorted_hand) > 0 and count_map[sorted_hand[0]] == 0:
                sorted_hand.pop(0)
            if len(sorted_hand) > 0:
                for key in range(sorted_hand[0], sorted_hand[0]+W):
                    if key in count_map:
                        count_map[key] -= 1
                        if count_map[key] < 0:
                            return False
                    else:
                        return False
        return True
