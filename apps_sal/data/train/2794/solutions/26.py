def calculate_age(year_of_birth, current_year):
    s = "s" if abs(current_year-year_of_birth) > 1 else ""
    return "You were born this very year!" if year_of_birth == current_year else f"You are {current_year - year_of_birth} year{s} old." if current_year > year_of_birth else f"You will be born in {year_of_birth-current_year} year{s}."
