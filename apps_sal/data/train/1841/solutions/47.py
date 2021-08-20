class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median: int = arr[(len(arr) - 1) // 2]
        ans: List[int] = []
        left: int = 0
        right: int = len(arr) - 1
        while len(ans) < k:
            if abs(arr[left] - median) > abs(arr[right] - median):
                ans.append(arr[left])
                left += 1
            else:
                ans.append(arr[right])
                right -= 1
        return ans
