class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        counter = collections.Counter(hand)
        while counter:
            smallest = min(counter)
            for j in range(smallest, smallest + W):
                if j not in counter:
                    return False
                counter[j] -= 1
                if counter[j] == 0:
                    del counter[j]
        return True
