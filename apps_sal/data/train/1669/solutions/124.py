import heapq
import collections


class Solution:
    def isNStraightHand(self, hand, W) -> bool:
        if len(hand) % W != 0:
            return False

        counter_map = collections.Counter(hand)
        counter = 0
        heapq.heapify(hand)

        while hand:
            min_val = heapq.heappop(hand)
            next_val = min_val + 1
            counter += 1
            while counter < W and counter_map.get(next_val, 0) > 0:
                counter_map[next_val] -= 1
                hand.remove(next_val)
                counter += 1
                next_val += 1

            # Cannot split anymore
            if counter < W:
                return False

            # resetting counter
            counter = 0
            heapq.heapify(hand)

        return True
