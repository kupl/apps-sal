from collections import defaultdict


class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand) < k or len(hand) % k != 0:
            return False
        if k == 1:
            return True
        hand.sort()

        queue = deque(hand)
        q2 = deque()

        currVal = -1
        currNum = 0
        for i in range(len(hand) // k):
            while currNum < k:
                if not queue:
                    return False
                if currVal == -1:
                    currVal = queue.popleft()
                    currNum += 1
                    continue
                val = queue.popleft()
                if val == currVal + 1:
                    currVal = val
                    currNum += 1
                elif val > currVal + 1:
                    return False
                elif val == currVal:
                    q2.append(val)

            queue = q2 + queue
            q2 = deque()
            currVal = -1
            currNum = 0
        return True
