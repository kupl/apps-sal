class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        ans = 0
        for i1,v1 in enumerate(arr):
            for i2, v2 in enumerate(arr[i1+1:]):
                if abs(v1 - v2) <= a:
                    for v3 in arr[i1 + i2 +2:]:
                        if abs(v1 - v3) <= c and abs(v2 - v3) <= b:
                            ans += 1
        return ans
