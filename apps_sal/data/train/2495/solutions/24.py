class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(len(target)):
            if target[i] in arr:
                arr.remove(target[i])
            else:
                pass
        if arr==[]:
            return True
        else:
            return False
