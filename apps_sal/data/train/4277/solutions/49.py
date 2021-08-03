def difference_in_ages(ages):
    an = ()
    minimum = min(ages)
    maximum = max(ages)
    diff = maximum - minimum
    an += minimum, maximum, diff
    return an
