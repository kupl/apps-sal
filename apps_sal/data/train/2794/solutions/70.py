def calculate_age(year_of_birth, current_year):
    y = current_year - year_of_birth
    if y == 1:
        return "You are 1 year old."
    elif y == -1:
        return "You will be born in 1 year."
    elif y > 1:
        return "You are {} years old.".format(y)
    elif y < -1:
        return "You will be born in {} years.".format(abs(y))
    elif y == 0:
        return "You were born this very year!"
