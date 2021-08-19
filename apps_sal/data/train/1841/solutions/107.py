class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        back = arr[:]
        n = len(arr)
        med = arr[(n - 1) // 2]
        ans = []
        for i in range(n):
            arr[i] = abs(arr[i] - med)
        (l, r) = (0, n - 1)
        while l <= r and len(ans) < k:
            if arr[l] < arr[r]:
                ans += [back[r]]
                r -= 1
            elif arr[l] > arr[r]:
                ans += [back[l]]
                l += 1
            else:
                ans += [back[r]]
                r -= 1
        return ans
