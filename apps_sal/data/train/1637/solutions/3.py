from bisect import bisect_left


def encode(s):
    if s == "":
        return ('', 0)

    # Pretend that I am a linked list with pointers to head and tail
    string_array = list(s)

    # Create the matrix
    matrix = []
    for _ in range(len(s)):
        # Shift the string array
        head = string_array.pop(0)
        string_array.append(head)

        # Add shifted array to the matrix
        matrix.append(list(string_array))

    # Sort the rows
    matrix.sort()

    # Get the last col string
    lost_col_array = []
    for row in matrix:
        lost_col_array.append(row[-1])

    # Now find the original string in the matrix
    row_num = bisect_left(matrix, string_array)
    return ("".join(lost_col_array), row_num)


def decode(s, n):
    if s == "":
        return ""

    matrix = []
    for index, char in enumerate(s):
        matrix.append([char])

    matrix.sort()

    # Do the following s - 1 times
    for _ in range(len(s) - 1):

        # Write out the encoded message and then sort
        for index, char in enumerate(s):
            matrix[index].insert(0, char)

        matrix.sort()

    return "".join(matrix[n])
