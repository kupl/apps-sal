class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goods = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    condition1 = abs(arr[i] - arr[j]) <= a
                    condition2 = abs(arr[j] - arr[k]) <= b
                    condition3 = abs(arr[i] - arr[k]) <= c
                    if condition1 and condition2 and condition3:
                        goods += 1
                        
        return goods
                    

