class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        (left, right) = (0, n - 1)
        result = []
        while k > 0 and left <= right:
            if arr[right] - median >= median - arr[left]:
                result.append(arr[right])
                right = right - 1
            else:
                result.append(arr[left])
                left = left + 1
            k = k - 1
        return result
