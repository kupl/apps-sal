def color(A, i, j):
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


def expand(A, level):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == level:
                if i > 0:
                    if A[i - 1][j] == 1:
                        return level
                    elif A[i - 1][j] == 0:
                        A[i - 1][j] = level + 1
                if j > 0:
                    if A[i][j - 1] == 1:
                        return level
                    elif A[i][j - 1] == 0:
                        A[i][j - 1] = level + 1
                if i < len(A) - 1:
                    if A[i + 1][j] == 1:
                        return level
                    elif A[i + 1][j] == 0:
                        A[i + 1][j] = level + 1
                if j < len(A) - 1:
                    if A[i][j + 1] == 1:
                        return level
                    elif A[i][j + 1] == 0:
                        A[i][j + 1] = level + 1
    return 0


class Solution:
    def shortestBridge(self, A):
        length = len(A)
        found = 0
        for i in range(len(A)):
            for j in range(len(A)):
                if A[i][j]:
                    found = 1
                    color(A, i, j)
                if found == 1:
                    break
            if found == 1:
                break

        level = 2
        found = 0
        while found == 0:
            found = expand(A, level)
            level += 1
        return found - 2
