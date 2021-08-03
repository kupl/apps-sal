def merge_arrays(first, second):
    array = sorted(first + second)
    array_num = [0]
    for i in array:
        if i != array_num[-1]:
            array_num.append(i)
        else:
            pass
    array_num.remove(0)
    return array_num
