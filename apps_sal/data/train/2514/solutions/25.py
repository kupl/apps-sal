class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        for i in range(len(arr1)):
            temp = 0
            for j in range(len(arr2)):
                if(abs(arr1[i] - arr2[j]) <= d):
                    temp = 1
                    break
            if(temp == 0):
                c += 1
        return c
