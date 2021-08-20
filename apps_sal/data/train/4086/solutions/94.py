def first_non_consecutive(arr):
    if len(arr) == 2:
        return None
    elem_1 = arr[0]
    elem_2 = arr[1]
    elem_3 = arr[2]
    diff_1 = elem_2 - elem_1
    diff_2 = elem_3 - elem_2
    if diff_1 > diff_2:
        grade_1 = diff_2
    elif diff_1 < diff_2:
        grade_1 = diff_1
    else:
        grade_1 = diff_1
    for i in range(0, len(arr) - 1):
        if arr[i + 1] != arr[i] + grade_1:
            return arr[i + 1]
    return None
