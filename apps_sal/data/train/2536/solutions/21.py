class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luck = []
        for i in arr:
            if arr.count(i) == i:
                luck.append(i)
        if luck:
            return max(luck)
        return -1
