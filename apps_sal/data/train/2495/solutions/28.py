from collections import defaultdict


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if (len(target) != len(arr)):
            return False

        numbers = defaultdict(int)
        for val in arr:
            numbers[val] += 1

        for val in target:
            numbers[val] -= 1

        print(numbers)

        if (min(numbers.values()) == 0 and max(numbers.values()) == 0):
            return True

        return False
