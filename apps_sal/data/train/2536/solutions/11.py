class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for i in sorted(set(arr)):
            if i == arr.count(i):
                ans = i
        return ans
