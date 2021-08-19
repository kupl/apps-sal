class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # size = len(arr)
        # res = 0
        # for i in range(size-2):
        #     for j in range(i+1, size-1):
        #         for k in range(j+1, size):
        #             ok_a = abs(arr[i] - arr[j]) <= a
        #             ok_b = abs(arr[j] - arr[k]) <= b
        #             ok_c = abs(arr[i] - arr[k]) <= c
        #             if all((ok_a, ok_b, ok_c)):
        #                 res += 1
        # return res

        res = (1 for i, j, k in combinations(arr, 3) if abs(i - j) <= a and abs(j - k) <= b and abs(i - k) <= c)
        return sum(res)
