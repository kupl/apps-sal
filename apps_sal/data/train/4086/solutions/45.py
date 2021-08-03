def first_non_consecutive(arr):
    is_consecutive = True
    for index, item in enumerate(arr[0:-1]):
        if item + 1 == arr[index + 1]:
            continue
        else:
            is_consecutive = False
            return arr[index + 1]
            break
    if is_consecutive == True:
        return None
