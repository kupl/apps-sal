class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:

        def encode_as_gray(n):
            return n ^ n >> 1
        arr = [encode_as_gray(i) for i in range(0, 2 ** n)]
        i = arr.index(start)
        return arr[i:] + arr[:i]
        return array[index:] + array[:index]
