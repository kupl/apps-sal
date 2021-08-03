def is_sorted_and_how(arr):
    counts = 0
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            counts += 1
        elif arr[index] < arr[index + 1]:
            counts -= 1

    if counts == len(arr) - 1:
        return "yes, descending"
    elif counts == -len(arr) + 1:
        return "yes, ascending"
    else:
        return "no"
