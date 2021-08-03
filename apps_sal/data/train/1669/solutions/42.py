class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        counter = Counter(hand)
        heap_hands = []
        groups = []
        for k, v in counter.items():
            heapq.heappush(heap_hands, (k, v))

        while(heap_hands):
            count = 0
            sub_group = []
            remaining_elements = []
            while(count < W):
                if not heap_hands:
                    return False
                popped_elem = heapq.heappop(heap_hands)
                if popped_elem[1] - 1 > 0:
                    remaining_elements.append(popped_elem)
                if not sub_group:
                    sub_group.append(popped_elem[0])
                else:
                    if popped_elem[0] - 1 == sub_group[-1]:
                        sub_group.append(popped_elem[0])
                    else:
                        return False
                count += 1

            groups += sub_group
            for elem in remaining_elements:
                heapq.heappush(heap_hands, (elem[0], elem[1] - 1))

        return True
