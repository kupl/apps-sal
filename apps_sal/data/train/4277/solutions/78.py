def difference_in_ages(ages):
    youngest_age = 10000000000000
    oldest_age = 0
    for x in ages:
        if x < youngest_age and x > oldest_age:
            youngest_age = x
            oldest_age = x
        elif x < youngest_age:
            youngest_age = x
        elif x > oldest_age:
            oldest_age = x
        else:
            pass
    difference = oldest_age - youngest_age
    return (youngest_age, oldest_age, difference)
