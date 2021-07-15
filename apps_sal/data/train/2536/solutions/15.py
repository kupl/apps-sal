class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort()
        luck = []
        for i in arr:
            if i == arr.count(i):
                luck.append(i)
        
        if len(luck) > 1:
            luck.sort()
            return luck[-1]
        
        if len(luck) == 1:
            return luck[0]
        
        return -1
