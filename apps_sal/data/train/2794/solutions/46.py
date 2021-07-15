def calculate_age(year_of_birth: int, current_year: int) -> str:
    """Year report depending on year of birth and current year."""
    def year_str(y:int) -> str:
        return "1 year" if y == 1 else str(y)+" years"
    delta = current_year - year_of_birth
    if delta == 0:
        return "You were born this very year!"
    elif delta > 0:
        return "You are " + year_str(delta) + " old."
    else:
        return "You will be born in " + year_str(-delta) + "."
