from collections import OrderedDict


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in range(m, m + W):
                v = count[k]
                if not v:
                    return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1

        return True
#         d = OrderedDict()

#         hand.sort()

#         # print(hand)
#         for val in hand:
#             if val in d:
#                 d[val] += 1
#             else:
#                 d.setdefault(val, 1)

#         i = 0
#         length = len(d)
#         items = list(d.items())
#         items = list(map(list, items))
#         while i <= length-W:
#             k, v = items[i]
#             if v == 0:
#                 i += 1
#                 continue
#             temp = W
#             j = i
#             prev = k
#             if j >= len(items):
#                 return False
#             while temp > 0:
#                 if items[j][0] != prev:
#                     return False
#                 else:
#                     items[j][1] -= 1
#                 j += 1
#                 prev = prev + 1
#                 temp -= 1
#                 if temp != 0 and j >= len(items):
#                     return False

#         for i in range(length-W, length):
#             k, v = items[i]
#             if v != 0:
#                 return False
#         return True
