class Solution:
  def isNStraightHand(self, hand, W):
    nums = len(hand)
    if nums % W: return False
    elif W == 1: return True
    else:
      heapify(hand)
      arrange = [[] for _ in range(nums//W)] 
      start = 0
      while hand:
        h = heappop(hand)
        i = start
        while True:
        #  print(h, i, arrange)
          if len(arrange[i]) == W:
            i += 1
            start = i
          if len(arrange[i]) == 0 or (arrange[i] and arrange[i][-1] != h):
            arrange[i].append(h)
          elif arrange[i] and arrange[i][-1] == h:
            if i+1 == len(arrange):
              return False
            i += 1
            continue
          if len(arrange[i]) > 1 and arrange[i][-2] + 1 != arrange[i][-1]:
            return False
          else:
            break

          #  return 
    return True #arrange
