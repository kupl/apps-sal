class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr:
            if i not in target:
                return 0
            else:
                target.remove(i)
        else:
            return 1
