class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        counter = Counter(hand)
        for i in range(len(hand) // W):
            minimum = min(counter.keys())
            for number in range(minimum, minimum + W):
                if number not in counter:
                    return False
                counter[number] -= 1
                if counter[number] == 0:
                    del counter[number]
        return True
