class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return k
        ans = 1
        idx = 0
        while k > 0:
            if idx < len(arr) and arr[idx] == ans:
                idx += 1
            else:
                k -= 1
                if k == 0:
                    break
            ans += 1
        return ans
