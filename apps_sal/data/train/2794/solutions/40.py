def calculate_age(year_of_birth, current_year):
    years = current_year - year_of_birth

    if years == 0:
        return "You were born this very year!"
    elif years == 1:
        return "You are 1 year old."
    elif years > 1:
        return f"You are {years} years old."
    elif years == -1:
        return "You will be born in 1 year."
    else:
        return f"You will be born in {abs(years)} years."
