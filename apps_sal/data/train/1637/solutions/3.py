from bisect import bisect_left


def encode(s):
    if s == "":
        return ('', 0)

    string_array = list(s)

    matrix = []
    for _ in range(len(s)):
        head = string_array.pop(0)
        string_array.append(head)

        matrix.append(list(string_array))

    matrix.sort()

    lost_col_array = []
    for row in matrix:
        lost_col_array.append(row[-1])

    row_num = bisect_left(matrix, string_array)
    return ("".join(lost_col_array), row_num)


def decode(s, n):
    if s == "":
        return ""

    matrix = []
    for index, char in enumerate(s):
        matrix.append([char])

    matrix.sort()

    for _ in range(len(s) - 1):

        for index, char in enumerate(s):
            matrix[index].insert(0, char)

        matrix.sort()

    return "".join(matrix[n])
