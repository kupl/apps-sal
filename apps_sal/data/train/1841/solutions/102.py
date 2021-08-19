class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        i = 0
        j = len(arr) - 1
        median = arr[(len(arr) - 1) // 2]
        while len(arr) + i - j <= k:
            if median - arr[i] > arr[j] - median:
                i += 1
            else:
                j -= 1
        return arr[:i] + arr[j + 1:]
