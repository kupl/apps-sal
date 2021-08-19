class Solution:

    def minIncrementForUnique(self, arr: List[int]) -> int:
        if not arr:
            return 0
        arr.sort()
        (s, ans) = (arr[0], 0)
        for i in arr:
            ans += max(0, s - i)
            s = max(s + 1, i + 1)
        return ans
