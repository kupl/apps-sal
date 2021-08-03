class Solution:
    def helper(self, n):
        return n ^ (n >> 1)

    def circularPermutation(self, n: int, start: int) -> List[int]:
        solution = list()
        for i in range(0, 2 ** n):
            solution.append(self.helper(i))
        index = -1
        for i in range(0, len(solution)):
            if solution[i] == start:
                index = i
                break
        # print(solution)
        return solution[index:] + solution[:index]
