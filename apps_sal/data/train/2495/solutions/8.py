class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if collections.Counter(target) != collections.Counter(arr):
            return False
        return True

        def reverse(left, right):
            while left < right:
                (arr[left], arr[right]) = (arr[right], arr[left])
                left += 1
                right -= 1
        for i in range(len(target)):
            if target[i] == arr[i]:
                continue
            j = arr.find(target[i])
            reverse(i, j)
