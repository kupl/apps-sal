def binary_cleaner(seq):
    less_than_1 = []
    index_list = []
    for i, x in enumerate(seq):
        if x < 2:
            less_than_1.append(x)
        if x > 1:
            index_list.append(i)
    return (less_than_1, index_list)
