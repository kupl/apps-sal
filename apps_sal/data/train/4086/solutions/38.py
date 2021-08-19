def first_non_consecutive(arr):
    for (number_lag, number) in zip(arr[:-1], arr[1:]):
        if number_lag + 1 != number:
            return number
    else:
        return None
