class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = Counter(hand)
        result = []
        while count:
            m = min(count)
            straights = []
            for i in range(m, m + W):
                if i in count:
                    straights.append(i)
                    count[i] -= 1
                    if count[i] == 0:
                        del count[i]
                else:
                    return False
            result.append(straights)
        print(result)
        return True
