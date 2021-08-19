class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        result = 0
        for i in range(0, size - 2):
            for j in range(i + 1, size - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, size):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result += 1
        return result
