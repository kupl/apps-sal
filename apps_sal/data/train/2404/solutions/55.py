class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected_value = 1
        i = 0
        while i < len(arr) and k > 0:
            if arr[i] != expected_value:
                k -= 1
            else:
                i += 1

            expected_value += 1

        while k > 0:
            expected_value += 1
            k -= 1

        return expected_value - 1

