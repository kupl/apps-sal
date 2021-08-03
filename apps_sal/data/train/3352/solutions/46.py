def find_longest(arr):
    highest_len = 0
    highest_len_name = 0
    for i in arr:
        if len(str(i)) > highest_len:
            highest_len = len(str(i))
            highest_len_name = i

    return highest_len_name
