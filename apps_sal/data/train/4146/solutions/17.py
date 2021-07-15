def is_sorted_and_how(a):
    if a == sorted(a):return 'yes, ascending'
    elif a == sorted(a, reverse=True):return 'yes, descending'
    else:return 'no'
