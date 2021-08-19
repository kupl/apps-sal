class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        count = 0
        arry = []
        while arr and len(arry) < k:
            if abs(arr[-1] - median) >= abs(arr[0] - median):
                arry.append(arr[-1])
                del arr[-1]
            else:
                arry.append(arr[0])
                del arr[0]
        return arry
