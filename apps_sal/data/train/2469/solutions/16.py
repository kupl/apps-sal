class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cache = set()
        for i, value in enumerate(arr):
            if 2 * value in cache or (value % 2 == 0 and value / 2 in cache):
                return True
            cache.add(value)
        return False
