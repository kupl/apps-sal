class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        straights, pq, = [], []
        for h in hand:
            heapq.heappush(pq, h)
        while len(pq) > 0:
            straight, dump = [], []
            while len(pq) > 0 and len(straight) < W:
                pop = heapq.heappop(pq)
                if len(straight) == 0 or pop == straight[-1] + 1:
                    straight.append(pop)
                else:
                    dump.append(pop)
            straights.append(straight)
            if len(straight) < W:
                return []
            else:
                for d in dump:
                    heapq.heappush(pq, d)

        return len(straights) > 0
