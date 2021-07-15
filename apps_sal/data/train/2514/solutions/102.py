class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for i in arr1:
            d_l = [abs(i-j) > d for j in arr2]
            if all(d_l):
                count += 1
        return count
                

