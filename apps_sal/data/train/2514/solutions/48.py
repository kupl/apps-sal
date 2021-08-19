class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # c=0
        # for a in arr1:
        #     t = 1
        #     for b in arr2:
        #         if abs(a-b)<=d:
        #             t*=0
        #         else:
        #             t*=1
        #     if t==1:
        #         c +=1
        # return c
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)
