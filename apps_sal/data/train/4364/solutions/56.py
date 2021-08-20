def odd_or_even(arr):
    added = sum(arr)
    if str(added)[-1] in '13579':
        return 'odd'
    else:
        return 'even'
    pass
