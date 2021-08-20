class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range(j, len(arr)):
                    num1 = arr[i] - arr[j]
                    num2 = arr[j] - arr[k]
                    num3 = arr[i] - arr[k]
                    if num1 < 0:
                        num1 = -num1
                    if num2 < 0:
                        num2 = -num2
                    if num3 < 0:
                        num3 = -num3
                    if num1 <= a and num2 <= b and (num3 <= c) and (0 <= i < j < k < len(arr)):
                        count += 1
        return count
