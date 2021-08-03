class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for num in arr:
            if num == 0:
                if arr.count(0) > 1:
                    return True
            else:
                if arr.count(num * 2) != 0:
                    return True
        return False
