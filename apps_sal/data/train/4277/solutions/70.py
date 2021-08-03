from operator import sub


def difference_in_ages(ages):
    """
        Returns a tuple with youngest age, oldest age, difference between
        the youngest and oldest age.
    """
    sort_ages = sorted(ages)
    return (sort_ages[0], sort_ages[-1], sub(sort_ages[-1], sort_ages[0]))
