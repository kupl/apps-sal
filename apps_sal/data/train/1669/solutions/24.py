class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Time: O(n*n/w)
        # Space: O(n)
        
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for j in range(m, m + W):
                if not count[j]:
                    return False
                if count[j] == 1:
                    del count[j]
                else:
                    count[j] -= 1
        return True
