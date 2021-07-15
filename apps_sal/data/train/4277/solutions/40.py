def difference_in_ages(ages):
    mx, mn = max(ages), min(ages)
    return (mx - mn, mx, mn)[::-1]
