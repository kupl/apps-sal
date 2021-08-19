class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for k in range(len(arr)):
            for j in range(k):
                if abs(arr[j] - arr[k]) <= b:
                    for i in range(j):
                        if abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[i]) <= a:
                            count += 1
        return count
