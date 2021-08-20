def difference_in_ages(ages):
    (lowest, highest) = (min(ages), max(ages))
    return (lowest, highest, highest - lowest)
