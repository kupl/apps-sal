def calculate_age(year_of_birth, current_year):
    if year_of_birth < current_year:
        yearsOld = current_year - year_of_birth
        if yearsOld == 1:
            return "You are " + str(yearsOld) + " year old."
        else:
            return "You are " + str(yearsOld) + " years old."
    elif year_of_birth > current_year:
        yearsOld = year_of_birth - current_year
        if yearsOld == 1:
            return "You will be born in " + str(yearsOld) + " year."
        else:
            return "You will be born in " + str(yearsOld) + " years."
    elif year_of_birth == current_year:
        yearsOld = year_of_birth
        return "You were born this very year!"
    # your code here
