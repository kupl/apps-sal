def sort_two_arrays(arr1, arr2):
    temp2 = [(i, v) for (i, v) in enumerate(arr2)]
    sorted_arr2_idx = [x[0] for x in sorted(temp2, key=lambda x: x[1])]
    temp1 = [(i, v) for (i, v) in enumerate(arr1)]
    sorted_arr1_idx = [x[0] for x in sorted(temp1, key=lambda x: x[1])]
    return [[arr1[sorted_arr2_idx[i]] for i in range(len(arr1))], [arr2[sorted_arr1_idx[i]] for i in range(len(arr1))]]
