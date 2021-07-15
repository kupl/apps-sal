def penultimate(a):
    # Check if list is empty or just one element, if yes return None
    if len(a) <= 1:
        return None
    # Else just return the second last element
    return a[len(a) - 2]
