class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        count = 0

        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for k in range(j + 1, len(arr)):

                    a_bool = abs(arr[i] - arr[j]) <= a
                    b_bool = abs(arr[j] - arr[k]) <= b
                    c_bool = abs(arr[i] - arr[k]) <= c

                    if a_bool and b_bool and c_bool:
                        count += 1

        return count
