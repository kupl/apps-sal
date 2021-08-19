def difference_in_ages(ages):
    # your code here
    youngest_age = min(ages)
    oldest_age = max(ages)
    difference = oldest_age - youngest_age
    return (youngest_age, oldest_age, difference)
