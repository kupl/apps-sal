def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth

    if age == 1:
        return "You are %s year old." % age
    if age > 1:
        return "You are %s years old." % age
    if age == 0:
        return "You were born this very year!"
    if age == -1:
        return "You will be born in %s year." % abs(age)

    else:
        return "You will be born in %s years." % abs(age)
