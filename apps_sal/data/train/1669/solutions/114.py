class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        d = collections.defaultdict(int)
        for i in hand:
            d[i] += 1
        while d:
            l = list(d)
            heapq.heapify(l)
            prev = None
            for i in range(W):
                if len(l) == 0:
                    return False
                ele = heapq.heappop(l)
                if prev is not None:
                    if ele - prev > 1:
                        return False
                prev = ele
                if d[ele] == 1:
                    del d[ele]
                else:
                    d[ele] -= 1
        return True
