def calculate_age(year_of_birth, current_year):
    years = abs(year_of_birth - current_year)
    if years == 1 and year_of_birth < current_year: return "You are 1 year old."
    if years == 1 and year_of_birth > current_year: return "You will be born in 1 year."
    return f"You are {years} years old." if year_of_birth < current_year else f"You will be born in {years} years." if year_of_birth > current_year else "You were born this very year!"
