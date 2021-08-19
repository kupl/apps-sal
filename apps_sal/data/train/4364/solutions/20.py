def odd_or_even(arr):
    if arr == []:
        return [0]
    elif sum(arr) > 0:
        if sum(arr) % 2 == 0:
            return 'even'
        else:
            return 'odd'
    elif sum(arr) < 0:
        if -1 * sum(arr) % 2 == 0:
            return 'even'
        else:
            return 'odd'
