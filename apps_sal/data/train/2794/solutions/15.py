def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age == 0:
        return "You were born this very year!"
    if age == 1:
        return "You are 1 year old."
    if age > 1:
        return "You are " + str(age) + " years old."
    if age == -1:
        return "You will be born in 1 year."
    return "You will be born in " + str(abs(age)) + " years."
