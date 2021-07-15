class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        
        for k, v in cnt.items():
            if v == max(cnt.values()):
                return k
