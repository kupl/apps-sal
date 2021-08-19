class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        missing = []
        # print(len(arr)+k)
        for num in range(1, len(arr) + k + 1):
            # print(num)
            if num not in arr:
                missing.append(num)

        # print(missing)
        return missing[k - 1]
