class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = []
        for i in range(2 ** n):
            gray.append(i ^ i >> 1)
            if start == i ^ i >> 1:
                index = i
        return gray[index:] + gray[0:index]
