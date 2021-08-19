class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr = sorted(arr)
        m = -1
        if n % 2 == 0:
            m = arr[(n - 1) // 2]
        else:
            m = arr[n // 2]
        ans = []
        left = 0
        right = n - 1
        while k > 0:
            if abs(arr[left] - m) > abs(arr[right] - m):
                ans.append(arr[left])
                left += 1
            else:
                ans.append(arr[right])
                right -= 1
            k -= 1
        return ans
