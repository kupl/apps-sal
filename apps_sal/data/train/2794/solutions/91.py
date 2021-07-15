def calculate_age(year_of_birth, current_year):
    years = current_year - year_of_birth
    if not years:
        return 'You were born this very year!'
    elif years > 0:
        return f'You are {years} year{"" if years == 1 else "s"} old.'
    return f'You will be born in {-years} year{"" if years == -1 else "s"}.'
