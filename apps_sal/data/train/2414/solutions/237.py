class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ot = 0
        n = len(arr)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, n):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    if abs(arr[i] - arr[k]) > c:
                        continue
                    ot +=1 
        return ot
