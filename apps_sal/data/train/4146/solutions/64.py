def is_sorted_and_how(A):
    S = sorted(A)
    if S == A:
        return 'yes, ascending'
    elif S == A[::-1]:
        return 'yes, descending'
    return 'no'
