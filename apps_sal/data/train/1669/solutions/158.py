import collections
import heapq


class Solution:
    def checkConsecutives(self, nums):
        pos = 0
        while pos < len(nums) - 1:
            if nums[pos][0] + 1 != nums[pos + 1][0]:
                return False
            pos += 1
        return True

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False

        min_heap = []
        heapq.heapify(min_heap)
        num_dict = collections.Counter(hand)
        for key, val in list(num_dict.items()):
            heapq.heappush(min_heap, (key, val))

        while min_heap:
            consec = []
            for _ in range(W):
                if not min_heap:
                    return False
                consec.append(list(heapq.heappop(min_heap)))

            if self.checkConsecutives(consec):
                pos = 0
                while pos < len(consec):
                    if consec[pos][1] - 1 <= 0:
                        consec.pop(pos)
                        continue
                    else:
                        consec[pos][1] -= 1
                    pos += 1
                pos = 0
                while pos < len(consec):
                    heapq.heappush(min_heap, tuple(consec[pos]))
                    pos += 1
            else:
                return False
        return True
