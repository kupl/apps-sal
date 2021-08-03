class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for k in range(len(arr) - 1):
            if 2 * arr[k] in arr[k + 1:] or 2 * arr[k] in arr[:k]:
                return True
        return False
