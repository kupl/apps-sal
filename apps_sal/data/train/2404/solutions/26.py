class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        missing_arr = [x + 1 for x in range(arr[-1] + 1) if x + 1 not in arr]
        # print(missing_arr)
        n = len(missing_arr)
        if k > n:
            return missing_arr[-1] + k - n
        return missing_arr[k - 1]
