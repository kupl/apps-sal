from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # def bin_search_variant(low, high, prev_val):
        #     mid = (high - low) // 2
        #     if arr[mid] == prev_val:
        #         return prev_val
        #     elif arr[mid]:
        #         if len(arr) == 1 or len(arr) == 2 or len(arr) == 3:
        #             return arr[0]

        #         cntr = Counter(arr).items()
        #         for k, v in cntr:
        #             if v > len(arr) / 4:
        #                 return k

        n = len(arr)
        if n <= 9:
            return self.findMode(arr)
        c = [
            arr[0],
            arr[(n - 1) // 8],
            arr[2 * (n - 1) // 8],
            arr[3 * (n - 1) // 8],
            arr[4 * (n - 1) // 8],
            arr[5 * (n - 1) // 8],
            arr[6 * (n - 1) // 8],
            arr[7 * (n - 1) // 8],
            arr[n - 1]
        ]
        return self.findMode(c)

    def findMode(self, arr: List[int]) -> int:
        # this findMode can be furthur optimized given the input is also non-descending
        return collections.Counter(arr).most_common(1)[0][0]
