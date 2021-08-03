def find_longest(arr):
    """This functino finds the first number with the most digits"""
    # for loop to iterate over numbers in list arr
    max_length = 0
    max_index = 0
    for cur_num in arr:
        length = len(str(cur_num))
        if length > max_length:
            max_length = length
            max_index = arr.index(cur_num)
    return arr[max_index]
