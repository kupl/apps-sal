def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 1:
        return "You are 1 year old."
    elif age == 0:
        return "You were born this very year!"
    elif age < -1:
        return "You will be born in " + str(-age) + " years."
    elif age == -1:
        return "You will be born in 1 year."
    else:
        return "You are " + str(age) + " years old."
