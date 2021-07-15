class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr1)
        m = len(arr2)
        count = 0
        for i in range(n):
            bad = False
            for j in range(m):
                if abs(arr1[i] - arr2[j]) <= d:
                    bad = True
            if not bad:
                count+=1
            
        return count

