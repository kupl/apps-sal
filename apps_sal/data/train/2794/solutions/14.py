def calculate_age(year_of_birth: int, current_year: int) -> str:
    """ Calculate how many years it was until a person would be born based on given data. """
    age = current_year - year_of_birth
    if age > 0:
        return f"You are {age} {'year' if age == 1 else 'years'} old."
    elif age < 0:
        return f"You will be born in {abs(age)} {'year' if abs(age) == 1 else 'years'}."
    else:
        return "You were born this very year!"
