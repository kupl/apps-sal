def sort_two_arrays(arr1, arr2):
    copy_arr1 = arr1[:]
    copy_arr2 = arr2[:]
    for i in range(len(arr1) - 1, 0, -1):
        for j in range(i):
            if copy_arr2[j] > copy_arr2[j + 1]:
                copy_arr2[j], copy_arr2[j + 1] = copy_arr2[j + 1], copy_arr2[j]
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
    for i in range(len(arr2) - 1, 0, -1):
        for j in range(i):
            if copy_arr1[j] > copy_arr1[j + 1]:
                copy_arr1[j], copy_arr1[j + 1] = copy_arr1[j + 1], copy_arr1[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
    return [arr1, arr2]
