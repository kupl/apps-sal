class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        result = all(elem in target for elem in arr)
        if result:
            return sorted(arr) == sorted(target)
        else:
            return False
