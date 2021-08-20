class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        for n in range(len(arr)):
            m = 2 * arr[n]
            for k in range(len(arr)):
                if arr[k] == m and k != n:
                    return True
        return False
