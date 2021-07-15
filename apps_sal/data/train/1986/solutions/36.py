class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        array = list(map(self.binaryToGray, range(0, 2 ** n)))
        index = array.index(start)

        return array[index: ] + array[: index]

    def binaryToGray(self, n: int) -> int:
        return n ^ (n >> 1)
