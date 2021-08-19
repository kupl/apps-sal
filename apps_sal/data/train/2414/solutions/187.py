class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def absolute(x):
            if x >= 0:
                return x
            return -x
        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if absolute(arr[i] - arr[j]) <= a and absolute(arr[j] - arr[k]) <= b and (absolute(arr[i] - arr[k]) <= c):
                        count += 1
        return count
