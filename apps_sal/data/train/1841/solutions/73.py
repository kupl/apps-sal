class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        median = sorted(arr)[(len(arr) - 1) // 2]
        
        # initial sort
        arr.sort()
        
        # sort based on |arr[i] - median|
        arr.sort(key=lambda x: abs(x - median))
        
        return arr[(len(arr) - k):]

