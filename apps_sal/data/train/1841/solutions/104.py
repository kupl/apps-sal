class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        lastPointer = -1
        startPointer = 0
        mInd = (len(arr)-1)//2
        m = arr[mInd]
        res = []
        for i in range(k):
            if abs(arr[lastPointer] - m) >= abs(arr[startPointer] - m):
                res.append(arr[lastPointer])
                lastPointer -= 1
            else:
                res.append(arr[startPointer])
                startPointer += 1
        return res

