class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        lookup = dict()
        for val in arr:
            if val * 2 in lookup:
                return True
            elif val / 2 in lookup:
                return True
            else:
                lookup[val] = 1
        return False
