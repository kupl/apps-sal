class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand_count = {}
        for x in hand:
            if x not in hand_count:
                hand_count[x] = 1
            else:
                hand_count[x] += 1

        while len(hand_count) > 0:
            min_key = min(hand_count.keys())
            min_key_count = hand_count[min_key]
            for i in range(W):
                key = min_key + i
                if key not in hand_count:
                    return False
                hand_count[key] -= min_key_count
                if hand_count[key] == 0:
                    del hand_count[key]
                elif hand_count[key] < 0:
                    return False
        return True
