class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0: return False
        counter = defaultdict(int)
        for elem in hand:
            counter[elem] += 1
        while len(counter) > 0:
            curr = min(counter.keys())
            counter[curr] -= 1
            if counter[curr] == 0:
                del counter[curr]
            for i in range(1,W):
                curr += 1
                if curr in counter:
                    counter[curr] -= 1
                    if counter[curr] == 0:
                        del counter[curr]
                else:
                    return False
        return True
