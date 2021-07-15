class Solution:
  # 204 ms
  def isNStraightHand(self, hand, W):
    nums = len(hand)
    if nums % W: return False
    elif W == 1: return True
    else:
      heapify(hand)
      arrange = deque() # collect group
      lastOp = [0,-1] # lastOp = [i, h]: record the operation of last time
      groups = 0 # count group
      while hand:
        h = heappop(hand)
        i = 0
        # if the same card as last time, escalate i
        if h == lastOp[1]: i = lastOp[0] + 1
        # add new group
        if len(arrange) < i+1:
          arrange.append([])
          groups += 1
        # num of group should be nums//W
        if groups > nums//W: return False
        # arrange new card if group size is less than W
        if len(arrange[i]) < W:
          arrange[i].append(h)
          lastOp = [i, h]
        # not consecutive, False
        if len(arrange[i]) > 1 and arrange[i][-2] + 1 != arrange[i][-1]:
          return False
        # pop group if size is full
        if len(arrange[i]) == W:
          arrange.popleft()
          lastOp = [0, -1]

    return True
