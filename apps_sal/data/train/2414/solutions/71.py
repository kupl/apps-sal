class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good=0
        arrLen=len(arr)
        for i in range(arrLen-2):
            for j in range(i+1, arrLen-1):
                for k in range(j+1, arrLen):
                    if arr[i] - arr[j] <= a and arr[j] - arr[i] <= a:
                        if arr[j] - arr[k] <= b and arr[k] - arr[j] <= b:
                            if arr[i] - arr[k] <= c and arr[k] - arr[i] <= c:
                                good+=1
        return good
