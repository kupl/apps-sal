class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        mp = {}
        for num in target:
            mp[num] = mp.get(num, 0) + 1
        for num in arr:
            if num not in mp:
                return False
            mp[num] -= 1
            if mp[num] < 0:
                return False
        return True
