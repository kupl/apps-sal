class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        counter = collections.Counter(hand)
        for num in hand:
            if counter[num - 1] > 0 or counter[num] == 0:
                continue
            curr = num
            cnt = 0
            while cnt < W:
                if counter[curr] == 0:
                    return False
                counter[curr] -= 1
                curr += 1
                cnt += 1
        return True
