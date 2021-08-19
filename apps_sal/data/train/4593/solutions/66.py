def merge_arrays(arr1, arr2):
    sort_1 = sorted(list(dict.fromkeys(arr1)))
    sort_2 = sorted(list(dict.fromkeys(arr2)))
    (one_index, two_index) = (0, 0)
    result = []
    while one_index < len(sort_1) and two_index < len(sort_2):
        if sort_1[one_index] == sort_2[two_index]:
            result.append(sort_1[one_index])
            one_index += 1
            two_index += 1
        elif sort_1[one_index] < sort_2[two_index]:
            result.append(sort_1[one_index])
            one_index += 1
        elif sort_1[one_index] > sort_2[two_index]:
            result.append(sort_2[two_index])
            two_index += 1
    result.extend(sort_1[one_index:])
    result.extend(sort_2[two_index:])
    return result
