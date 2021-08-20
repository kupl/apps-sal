def first_non_consecutive(arr):
    first_ele = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == first_ele + 1:
            first_ele = first_ele + 1
        else:
            return arr[i]
