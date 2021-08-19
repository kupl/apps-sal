"""
go through each array,
keep track of duplicate elements using a hash
if it doesn exist store it in final array.
"""


def unite_unique(*arrays):
    final = []
    table = {}
    for array in arrays:
        for elem in array:
            if elem not in final:
                final.append(elem)
    return final
