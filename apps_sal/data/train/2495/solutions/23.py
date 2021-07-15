class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        for i in range(len(target)):
            if target[i] not in arr:
                return False
            if target[i] in arr:
                arr[arr.index(target[i])]  = 0
        return True

