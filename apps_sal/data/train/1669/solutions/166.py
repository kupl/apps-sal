class Solution:
    import heapq
    # https://www.youtube.com/watch?v=Zz7BWDY5kvM&list=UUSYPN_WIvDy4spjxzdevk6Q

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if W == 1:
            return True
        if len(hand) % W:
            return False
        hand.sort()
        heap = []
        for n in hand:
            if not heap:
                heapq.heappush(heap, (n, 1))
            else:
                curr, size = heap[0]
                if n == curr:
                    heapq.heappush(heap, (curr, 1))
                elif n == curr + 1:
                    heapq.heappop(heap)
                    size += 1
                    if size < W:
                        heapq.heappush(heap, (n, size))
                else:
                    return False
        return bool(not heap)
