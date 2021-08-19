class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in range(len(target)):
            if target[i] not in arr:
                return False
            arr.pop(arr.index(target[i]))
        return True
