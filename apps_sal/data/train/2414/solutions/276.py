class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # Base case
        if len(arr) < 3:
            return 0
        
        result = 0
        
        for i in range(len(arr) - 2):
            num1 = arr[i]
            for j in range(i + 1, len(arr) - 1):
                num2 = arr[j]
                
                for k in range(j + 1, len(arr)):
                    num3 = arr[k]
                    
                    if abs(num1 - num2) <= a and abs(num2 - num3) <= b and abs(num3 - num1) <= c:
                        result += 1
                        
        return result
