class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n - 1) // 2]
        l = 0
        r = n - 1
        ans = []
        while len(ans) != k:
            if abs(m - arr[l]) > abs(arr[r] - m):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
        return ans
