def calculate_age(year_of_birth, current_year):
    a = abs(current_year - year_of_birth)
    if not a:
        return 'You were born this very year!'
    else:
        return (f"You are {a} year{('', 's')[a > 1]} old.", f"You will be born in {a} year{('', 's')[a > 1]}.")[current_year < year_of_birth]
