class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in target:
            if i not in arr:
                return False
            arr[arr.index(i)] = None
        return True
