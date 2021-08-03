def calculate_age(year_of_birth, current_year):

    age = abs(current_year - year_of_birth)

    if year_of_birth < current_year:
        return f"You are {age} years old." if age > 1 else f"You are {age} year old."
    elif year_of_birth > current_year:
        return f"You will be born in {age} years." if age > 1 else f"You will be born in {age} year."
    else:
        return f"You were born this very year!"
