class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        sortedR1 = rec1
        if rec1[0] > rec1[2]:
            sortedR1[0] = rec1[2]
            sortedR1[2] = rec1[0]
        if rec1[1] > rec1[3]:
            sortedR1[1] = rec1[3]
            sortedR1[3] = rec1[1]
        sortedR2 = rec2
        if rec2[0] > rec2[2]:
            sortedR2[0] = rec2[2]
            sortedR2[2] = rec2[0]
        if rec2[1] > rec2[3]:
            sortedR2[1] = rec2[3]
            sortedR2[3] = rec2[1]

#         if (sortedR1[0] == sortedR1[2]) or (sortedR1[1] == sortedR1[3]):
#             return False
#         if (sortedR2[0] == sortedR2[2]) or (sortedR2[1] == sortedR2[3]):
#             return False

#         if (sortedR2[0] < sortedR1[2] <= sortedR2[2]):
#             if (sortedR2[1] < sortedR1[3] <= sortedR2[3]):
#                 return True
#             elif (sortedR2[1] <= sortedR1[1] < sortedR2[3]):
#                 return True
#             else:
#                 return False

#         if (sortedR2[0] <= sortedR1[0] < sortedR2[2]):
#             if (sortedR2[1] < sortedR1[3] <= sortedR2[3]):
#                 return True
#             elif (sortedR2[1] <= sortedR1[1] < sortedR2[3]):
#                 return True
#             else:
#                 return False
#         print('ok')

        if (sortedR2[0] < sortedR1[2]) and (sortedR2[2] > sortedR1[0]):
            if (sortedR2[1] < sortedR1[3]) and (sortedR2[3] > sortedR1[1]):
                return True
        return False
