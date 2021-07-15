class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        def helper(arr):
            if abs(arr[0]-arr[1]) <= a and abs(arr[1]-arr[2]) <= b and abs(arr[0]-arr[2]) <= c:
                return True
            else:
                return False
        
        result = 0
        
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                    idx = (arr[i], arr[j], arr[k])
                    if helper(idx):
                        result += 1
        
        return result
                            

