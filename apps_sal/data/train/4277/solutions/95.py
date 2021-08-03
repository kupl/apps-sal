def difference_in_ages(ages):
    minage = min(ages)
    maxage = max(ages)
    return (minage, maxage, abs(maxage - minage))
