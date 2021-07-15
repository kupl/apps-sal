class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = 0
        for i in range(len(arr1)):
            f = 0
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j])<=d:
                    f = 1
            if f==1:
                c+=1
        return(len(arr1) - c)

