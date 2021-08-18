class Solution:
    def isNStraightHand(self, hand, W):
        nums = len(hand)
        if nums % W:
            return False
        elif W == 1:
            return True
        else:
            heapify(hand)
            arrange = deque()
            lastOp = [0, -1]
            groups = 0
            while hand:
                h = heappop(hand)
                i = 0
                if h == lastOp[1]:
                    i = lastOp[0] + 1
                if len(arrange) < i + 1:
                    arrange.append([])
                    groups += 1
                if groups > nums // W:
                    return False
                if len(arrange[i]) and arrange[i][-1] + 1 != h:
                    return False
                else:
                    arrange[i].append(h)
                    lastOp = [i, h]
                if len(arrange[i]) == W:
                    arrange.popleft()
                    lastOp = [0, -1]

        return True
