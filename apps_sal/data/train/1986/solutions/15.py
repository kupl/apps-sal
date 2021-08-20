class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:

        def extendPerm(arr):
            arr.extend(['1' + num for num in arr[::-1]])
            for i in range(len(arr) // 2):
                arr[i] = '0' + arr[i]
        arr = ['0', '1']
        for i in range(n - 1):
            extendPerm(arr)
        nums = [int(num, 2) for num in arr]
        index = nums.index(start)
        return nums[index:] + nums[:index]
