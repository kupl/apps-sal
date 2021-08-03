class Solution:
    def isMonotonic(self, a: List[int]) -> bool:
        #         n = len(a)

        #         if n == 1:
        #             return True

        #         asc = True if a[n-1] - a[0] >= 0 else False

        #         for i in range(1, n):
        #             if asc:
        #                 if a[i] - a[i-1] < 0:
        #                     return False
        #             else:
        #                 if a[i] - a[i-1] > 0:
        #                     return False

        #         return True

        increasing = decreasing = True

        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                increasing = False
            if a[i] < a[i + 1]:
                decreasing = False

        return increasing or decreasing


'''
[1,2,2,3]
[6,5,4,4]
[1,3,2]
[1,2,4,5]
[1,1,1]
[1,2,3,4,0]
'''
