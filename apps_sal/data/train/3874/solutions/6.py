def sort_twisted37(arr):
    str_arr = [str(i) for i in arr]
    swap1(str_arr)
    str_arr = sorted([int(i) for i in str_arr])
    str_arr = [str(i) for i in str_arr]
    swap1(str_arr)
    return [int(i) for i in str_arr]


def swap1(str_arr):
    for (index, numstr) in enumerate(str_arr):
        if '3' in numstr or '7' in numstr:
            str_arr[index] = numstr.replace('3', '%temp%').replace('7', '3').replace('%temp%', '7')
