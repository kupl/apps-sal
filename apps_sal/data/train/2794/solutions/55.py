def calculate_age(year_of_birth, current_year):
    s='s'
    if current_year>year_of_birth:
        return f'You are {current_year-year_of_birth} year{s if current_year-year_of_birth!=1 else ""} old.'
    if year_of_birth>current_year:
        return f'You will be born in {year_of_birth-current_year} year{s if -current_year+year_of_birth!=1 else ""}.'
    if year_of_birth==current_year:
        return 'You were born this very year!'

