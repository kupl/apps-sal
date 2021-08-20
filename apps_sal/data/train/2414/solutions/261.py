class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        result = 0
        res = []
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, size):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            result += 1
                            res.append((arr[i], arr[j], arr[k]))
        return result
