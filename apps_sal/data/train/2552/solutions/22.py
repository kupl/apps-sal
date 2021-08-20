class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        unique_values = list()
        for i in range(0, len(arr)):
            if arr[i] not in unique_values:
                unique_values.append(arr[i])
        for j in range(0, len(unique_values)):
            if arr.count(unique_values[j]) / len(arr) > 0.25:
                return unique_values[j]
