def difference_in_ages(ages):
    youngest_age = ages[0]
    oldest_age = 0
    
    for age in ages:
        if age < youngest_age:
            youngest_age = age
        if age > oldest_age:
            oldest_age = age
    
    soln = (youngest_age, oldest_age, oldest_age-youngest_age)
    return soln

