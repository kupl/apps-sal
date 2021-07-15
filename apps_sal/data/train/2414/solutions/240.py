class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count    = 0
        size_arr = len(arr)

        for i in range(size_arr - 2):
            for j in range(i + 1, size_arr - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue

                for k in range(j + 1, size_arr):
                    if abs(arr[j] - arr[k]) > b:
                        continue

                    if abs(arr[i] - arr[k]) > c:
                        continue

                    count += 1

        return count
