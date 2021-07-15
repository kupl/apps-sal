def sort_by_bit(arr):
    return [val[1] for val in sorted([["{0:b}".format(val).count('1'),val] for val in arr])]
