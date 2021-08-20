class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        if len(hand) == 0:
            return True
        hand = sorted(hand)
        '\n        hand_dict = {}\n\n        for h in hand:\n            if h in hand_dict:\n                hand_dict[h]+=1\n            else:\n                hand_dict[h]=1\n\n        print(hand_dict)\n        '
        seed = hand[0]
        for i in range(1, W):
            if seed + i not in hand:
                return False
        for i in range(0, W):
            hand.remove(seed + i)
        return self.isNStraightHand(hand, W)
