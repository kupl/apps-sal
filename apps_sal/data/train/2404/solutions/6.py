class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] > k:
            return k
        else:
            k = k - arr[0] + 1
        for index in range(1, len(arr)):
            if k > arr[index] - arr[index - 1] - 1:
                k = k - (arr[index] - arr[index - 1] - 1)
            else:
                return arr[index - 1] + k
        if k > 0:
            return arr[-1] + k
