class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        #         hand.sort()

        #         mask = 0

        #         i = 0
        #         while i < len(hand):
        #             lst = -1
        #             k = 0
        #             j = 0
        #             for j in range(len(hand)):
        #                 if mask & (1 << j) > 0:
        #                     continue
        #                 elif lst == -1 or lst == hand[j] - 1:
        #                     mask = mask | (1 << j)
        #                     lst = hand[j]
        #                     k += 1
        #                     i += 1
        #                     if k == W:
        #                         break

        #             if k != W:
        #                 return False

        #         return True

        counter = collections.Counter(hand)

        while counter:
            m = min(counter)
            for k in range(m, m + W):

                if not counter[k]:
                    return False

                counter[k] -= 1

                if counter[k] == 0:
                    del counter[k]
        return True
