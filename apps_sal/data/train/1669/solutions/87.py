class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        flag = 0
        while len(hand) > 0 and flag == 0:
            temp = []
            start = hand[0]
            temp.append(start)
            for i in range(1, W):
                if start + i in hand:
                    temp.append(start + i)
                else:
                    flag = 1
                    break
            for x in temp:
                hand.remove(x)
        if flag == 0:
            return True
        else:
            return False
