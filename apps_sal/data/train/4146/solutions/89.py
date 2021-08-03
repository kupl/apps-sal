def is_sorted_and_how(arr):
    sarr = sorted(arr)
    return "yes, ascending" if sarr == arr else "yes, descending" if sarr[::-1] == arr else "no"
