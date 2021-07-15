class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1, len(arr)):
                        res1 = abs(arr[i] - arr[j]) <= a
                        res2 = abs(arr[j] - arr[k]) <= b
                        res3 = abs(arr[i] - arr[k]) <= c

                        if all((res1, res2, res3)):
                            count += 1

        return count

