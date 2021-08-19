class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        is_monotonic_incr = True
        is_monotonic_desc = True
        array1 = A
        for num in range(1, len(array1)):
            if array1[num] < array1[num - 1]:
                print('in first if', array1[num], array1[num - 1])
                is_monotonic_incr = False
            if array1[num] > array1[num - 1]:
                print('in second if', array1[num], array1[num - 1])
                is_monotonic_desc = False
        return is_monotonic_incr or is_monotonic_desc
