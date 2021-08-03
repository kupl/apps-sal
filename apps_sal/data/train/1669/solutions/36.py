class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)

        while counter:
            num = min(counter)

            for _ in range(W):
                if num not in counter:
                    return False

                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]

                num += 1

        return True
