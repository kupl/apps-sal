class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        (counter, smallest) = self.counter(hand)
        for _ in range(len(hand) // W):
            if smallest is None:
                smallest = min(counter)
            curr = smallest
            counter[curr] -= 1
            if counter[curr] == 0:
                del counter[curr]
                smallest = None
            for _ in range(W - 1):
                curr = curr + 1
                if curr not in counter:
                    return False
                else:
                    counter[curr] -= 1
                    if counter[curr] == 0:
                        del counter[curr]
                    elif smallest is None:
                        smallest = curr
        return True

    def counter(self, array):
        smallest = None
        counter = {}
        for el in array:
            if el in counter:
                counter[el] += 1
            else:
                counter[el] = 1
                if smallest is None or el < smallest:
                    smallest = el
        return (counter, smallest)
