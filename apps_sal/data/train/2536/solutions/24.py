class Solution:

    def findLucky(self, arr: List[int]) -> int:
        num = -1
        for c in arr:
            if c == arr.count(c):
                num = max(num, c)
        return num
