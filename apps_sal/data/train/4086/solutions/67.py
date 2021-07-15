def first_non_consecutive(arr):
    new_list = arr.pop(0)
    for num in arr:
        new_list += 1
        if num != new_list:
            return num

