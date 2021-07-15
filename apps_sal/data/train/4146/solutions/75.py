def is_sorted_and_how(arr):
    return 'yes, %sscending' % ['a', 'de'][max(sorted(arr)) == arr[0]] if sorted(arr)[0] in [arr[0], arr[-1]] else 'no'
