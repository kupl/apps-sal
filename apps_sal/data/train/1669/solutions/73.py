class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            mins = min(count)
            for i in range(mins, mins + W):
                if not count[i]:
                    return False
                if count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1
        return True
        # heapq.heapify(hand)
        # while hand:
        #     mins = hand[0]
        #     #print(hand)
        #     for i in range(mins, mins + W):
        #         #print(i)
        #         if i in hand:
        #             hand.remove(i)
        #             heapq.heapify(hand)
        #         else:
        #             return False
        # return True
