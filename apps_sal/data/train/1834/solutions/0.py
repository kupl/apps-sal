class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:

        def bitFlip(row):

            for i, r in enumerate(row):
                row[i] = 1 - r

            return row

        for i, row in enumerate(A):
            if row[0] == 0:
                A[i] = bitFlip(row)

        for j in range(1, len(A[0])):
            count = 0
            for i in range(0, len(A)):
                count += A[i][j]
            if count <= len(A) // 2:
                for i in range(0, len(A)):
                    A[i][j] = 1 - A[i][j]

        def score(row):

            return sum([r * 2**i for i, r in enumerate(reversed(row))])

        return sum([score(row) for row in A])
