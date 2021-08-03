def is_sorted_and_how(arr):
    check = [arr[i - 1] < arr[i] for i in range(1, len(arr))]
    true = check.count(True)
    false = check.count(False)
    if true == len(arr) - 1 and false == 0:
        return 'yes, ascending'
    elif false == len(arr) - 1 and true == 0:
        return 'yes, descending'
    else:
        return 'no'
