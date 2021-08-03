class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goods = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                condition1 = abs(arr[i] - arr[j]) <= a
                if not condition1:
                    continue
                for k in range(j + 1, len(arr)):
                    condition2 = abs(arr[j] - arr[k]) <= b
                    condition3 = abs(arr[i] - arr[k]) <= c
                    if condition2 and condition3:
                        goods += 1

        return goods
