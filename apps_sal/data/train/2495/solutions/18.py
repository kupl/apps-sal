class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for a in arr:
            if a in target:
                target.remove(a)
            else:
                return False
        return True
