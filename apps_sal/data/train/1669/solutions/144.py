class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        heapq.heapify(hand)
        while hand:
            last_item = heapq.heappop(hand)
            leftover = []
            for _ in range(W - 1):
                if not hand:
                    return False
                next_item = heapq.heappop(hand)
                while next_item == last_item:
                    leftover.append(next_item)
                    if not hand:
                        return False
                    next_item = heapq.heappop(hand)
                if next_item > last_item + 1:
                    return False
                last_item = next_item
            for item in leftover:
                heapq.heappush(hand, item)
        return True
