from itertools import count

def smallest_integer(matrix):
    nums = {n for row in matrix for n in row}
    for i in count():
        if i not in nums:
            return i
