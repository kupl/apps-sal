class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        for i in arr1:
            add=1
            for j in range(d+1):
                if (i+j) in arr2 or (i-j) in arr2:
                    add=0
                    break
            count+=add
        return count
