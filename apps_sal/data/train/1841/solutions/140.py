class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        ans = []
        left, right = 0, len(arr) - 1
        for _ in range(k):
            if abs(arr[right] - m) >= abs(arr[left] - m):
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1
        return ans
