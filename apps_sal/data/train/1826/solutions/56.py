class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prev = 0
        answer = []
        for row in range(len(mat)):
            answer.append([])
            for col in range(len(mat[0])):
                l = max(0, col - k)
                r = min(col + k + 1, len(mat[0]))
                t = max(0, row - k)
                b = min(row + k + 1, len(mat))
                submat = [mat[i][l:r] for i in range(t, b)]
                total = 0
                for one in submat:
                    for two in one:
                        total += two
                answer[-1].append(total)
        return answer
