class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W:
            return False
        counter = Counter(hand)
        keys = set(counter.keys())
        while counter:
            key = min(keys)
            while key in keys:
                for w in range(W):
                    if key + w not in counter:
                        return False
                    counter[key + w] -= 1
                    if counter[key + w] == 0:
                        del counter[key + w]
                        keys.remove(key + w)
        return True
