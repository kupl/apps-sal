class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    val1 = arr[j]-arr[k]
                    val2 = arr[i] - arr[k]
                    val = arr[i] - arr[j]
                    if abs(val) <= a and abs(val1) <= b and abs(val2) <= c:
                        ans +=1
            
        return ans
