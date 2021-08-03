class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr = []
        for i in range(len(arr1)):
            count = 0
            for j in range(len(arr2)):
                if(abs(arr1[i] - arr2[j]) <= d):
                    count = count + 1
            if(count == 0):
                arr.append(arr1[i])
        return len(arr)
