def color(A, i, j):
    if A[i][j] in (0, 2):
        return
    A[i][j] = 2
    if i > 0:
        if A[i - 1][j] == 1:
            color(A, i - 1, j)
    if j > 0:
        if A[i][j - 1] == 1:
            color(A, i, j - 1)
    if i < len(A) - 1:
        if A[i + 1][j] == 1:
            color(A, i + 1, j)
    if j < len(A) - 1:
        if A[i][j + 1] == 1:
            color(A, i, j + 1)


def expand(A):
    for l in range(2, len(A) ** 2):
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j] == l:
                    if i > 0:
                        if A[i - 1][j] == 0:
                            A[i - 1][j] = l + 1
                        if A[i - 1][j] == 1:
                            return l - 2
                    if j > 0:
                        if A[i][j - 1] == 0:
                            A[i][j - 1] = l + 1
                        if A[i][j - 1] == 1:
                            return l - 2
                    if i < len(A) - 1:
                        if A[i + 1][j] == 0:
                            A[i + 1][j] = l + 1
                        if A[i + 1][j] == 1:
                            return l - 2
                    if j < len(A) - 1:
                        if A[i][j + 1] == 0:
                            A[i][j + 1] = l + 1
                        if A[i][j + 1] == 1:
                            return l - 2


class Solution:

    def shortestBridge(self, A):
        length = len(A)
        found = 0
        for i in range(length):
            for j in range(length):
                if A[i][j]:
                    color(A, i, j)
                    found = 1
                    break
            if found == 1:
                break
        expansion = expand(A)
        return expansion
