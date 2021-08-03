class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)

        while count:
            minCount = min(count)

            for i in range(minCount, minCount + W):
                if not count[i]:  # if i not in count:
                    return False
                if count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1
        return True
