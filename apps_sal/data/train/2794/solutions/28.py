def calculate_age(year_of_birth, current_year):
    difference = current_year - year_of_birth
    if difference == 1:
        return "You are 1 year old."
    if difference == -1:
        return "You will be born in 1 year."
    if difference > 0:
        return "You are {difference} years old.".format(difference=difference)
    if difference == 0:
        return "You were born this very year!"
    else:
        difference = abs(difference)
        return "You will be born in {difference} years.".format(difference=difference)
