def check_exam(arr1, arr2):
    ret = 0
    for pair in zip(arr1, arr2):
        if pair[1] == '':
            continue
        ret += 4 if pair[0] == pair[1] else -1
    return max(0, ret)
