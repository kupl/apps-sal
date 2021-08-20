def find_longest(arr):
    max_lenght = 0
    max_index = 0
    for cur_num in arr:
        lenght = len(str(cur_num))
        if lenght > max_lenght:
            max_lenght = lenght
            max_index = arr.index(cur_num)
    return arr[max_index]
