def difference_in_ages(ages):
    age_min, age_max = min(ages), max(ages)
    return (age_min, age_max, age_max - age_min)
