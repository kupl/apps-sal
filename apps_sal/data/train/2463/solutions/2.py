class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        arr = A
        if len(arr) < 3:
            return False
        if arr[0] > arr[1]:
            return False
        if arr[-1] > arr[-2]:
            return False
        
        peek = None
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i+1]:
                peek = i
            if peek and arr[i] < arr[i+1]:
                return False
            if arr[i] == arr[i+1] or arr[i] == arr[i-1]:
                return False
        return True
