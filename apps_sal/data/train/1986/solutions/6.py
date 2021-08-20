class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = []
        for i in range(2 ** n):
            gray.append(i ^ i >> 1)
        idxStart = gray.index(start)
        result = []
        for i in range(len(gray)):
            result.append(gray[(i + idxStart) % len(gray)])
        return result
