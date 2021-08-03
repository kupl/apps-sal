class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand = sorted(hand)
        indices = {}
        for index in reversed(list(range(len(hand)))):
            num = hand[index]
            if num not in indices:
                indices[num] = [index]
            else:
                indices[num].append(index)
        while len(indices) != 0:
            first = None
            for num in hand:
                if num in indices:
                    first = num
                    break
            for i in range(W):
                num = first + i
                if num in indices:
                    indices[num].pop()
                    if len(indices[num]) == 0:
                        del indices[num]
                else:
                    return False
        return True
