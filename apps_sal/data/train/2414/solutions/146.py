class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        count = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                check_a = abs(arr[i] - arr[j]) <= a
                for k in range(j+1,len(arr)):
                    
                    check_b = abs(arr[j] - arr[k]) <= b
                    check_c = abs(arr[i] - arr[k]) <= c
                    
                    if all([check_a,check_b,check_c]):
                        count += 1
                            
        return count
