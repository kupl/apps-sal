class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        cnt = 0
        
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                for k in range(0, len(arr)):
                    if(i < j < k):
                        if(abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                            cnt = cnt + 1
        
        return cnt

