class Solution:
    def isMonotonic(self, a: List[int]) -> bool:

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
