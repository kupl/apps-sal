class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if len(hand) % W != 0:
            return False

        if len(hand) == 0:
            return True

        hand = sorted(hand)

        '''
        hand_dict = {}

        for h in hand:
            if h in hand_dict:
                hand_dict[h]+=1
            else:
                hand_dict[h]=1

        print(hand_dict)
        '''

        seed = hand[0]

        for i in range(1, W):

            if seed + i not in hand:
                return False

        for i in range(0, W):
            hand.remove(seed + i)

        return self.isNStraightHand(hand, W)
