class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # this is basically a buble sort kinda technique, but not sorted
        # if need to do this then??
        # put first element in place based on target
        # reverse from i to numIndex
        # increase i
        
        # or iterate both at the same time and check for 0 at the end
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
        
        

