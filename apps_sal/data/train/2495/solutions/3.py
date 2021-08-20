class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sum(arr) != sum(target):
            return False
        boolean = True
        for (i, v) in enumerate(target):
            if v in arr:
                boolean = True & boolean
            else:
                boolean = False & boolean
                break
        return boolean
