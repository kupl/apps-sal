class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = (len(arr) - 1) // 2
        i = 0
        j = len(arr) - 1
        result = []
        while i <= j and len(result) < k:
            if abs(arr[i] - arr[m]) > abs(arr[j] - arr[m]):
                result.append(arr[i])
                i += 1
            else:
                result.append(arr[j])
                j -= 1
        return result
