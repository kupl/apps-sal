class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        arrsize = len(arr)
        for i in range(0, arrsize - 2):
            for j in range(i + 1, arrsize - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, arrsize):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            count += 1
                        
        return count
