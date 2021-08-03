def is_sorted_and_how(arr):
    return next(('yes, {}cending'.format(k) for k, v in {'as': sorted(arr), 'des': sorted(arr, reverse=True)}.items() if v == arr), 'no')
