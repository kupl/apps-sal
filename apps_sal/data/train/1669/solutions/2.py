class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        heap = [(key, val) for key, val in list(Counter(hand).items())]
        heapq.heapify(heap)
        while heap:
            pre, prec = None, None
            temp = deque()
            for _ in range(W):
                if not heap:
                    return False
                num, count = heapq.heappop(heap)
                if not pre:
                    pre, prec = num, count
                    continue
                if num != pre + 1 or count < prec:
                    return False
                pre = num
                if count > prec:
                    temp.append((num, count - prec))
            while temp:
                heapq.heappush(heap, temp.pop())
        return True
