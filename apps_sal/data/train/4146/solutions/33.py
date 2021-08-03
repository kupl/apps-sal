def is_sorted_and_how(arr):
    monity = arr[1] <= arr[0]
    for index in range(len(arr))[2:]:
        if (arr[index] <= arr[index - 1]) != monity:
            return "no"
    return "yes, descending" if monity else "yes, ascending"
