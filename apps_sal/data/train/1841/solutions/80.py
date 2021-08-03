class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        count = 0
        arry = []
        while arr and len(arry) < k:
            if (arr[-1] - median) >= (median - arr[0]):
                arry.append(arr[-1])
                del arr[-1]
            else:
                arry.append(arr[0])
                del arr[0]

        return arry
