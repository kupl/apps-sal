class Solution:

    def isNStraightHand(self, h: List[int], W: int) -> bool:
        l = len(h)
        if l % W != 0:
            return False
        heapify(h)
        c = Counter(h)
        for _ in range(l // W):
            x = heappop(h)
            while c[x] == 0:
                x = heappop(h)
            for _ in range(W):
                if c[x] == 0:
                    return False
                c[x] -= 1
                x += 1
        return True
