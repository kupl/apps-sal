class Solution:
    def canBeEqual(self, target, arr) -> bool:
        
        target = sorted(target)
        arr = sorted(arr)

        return target == arr
