class Solution:
    # 204 ms
    def isNStraightHand(self, hand, W):
        nums = len(hand)
        if nums % W:
            return False
        elif W == 1:
            return True
        else:
            heapify(hand)
            arrange = deque()  # collect group
            lastOp = [0, -1]  # lastOp = [i, h]: record the operation of last time
            groups = 0  # count group
            while hand:
                h = heappop(hand)
                i = 0
                # if the same card as last time, escalate i
                if h == lastOp[1]:
                    i = lastOp[0] + 1
                # add new group
                if len(arrange) < i + 1:
                    arrange.append([])
                    groups += 1
                # num of group should be nums//W
                if groups > nums // W:
                    return False
                # not consecutive, False
                if len(arrange[i]) and arrange[i][-1] + 1 != h:
                    return False
                else:
                    # arrange new card if group size is less than W
                    arrange[i].append(h)
                    lastOp = [i, h]
                # pop group if size is full
                if len(arrange[i]) == W:
                    arrange.popleft()
                    lastOp = [0, -1]

        return True
