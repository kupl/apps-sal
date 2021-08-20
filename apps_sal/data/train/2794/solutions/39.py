def calculate_age(year_of_birth, current_year):
    age = current_year - year_of_birth
    if age > 0:
        return f'You are {age} years old.' if age > 1 else 'You are 1 year old.'
    if age < 0:
        return 'You will be born in 1 year.' if age == -1 else f'You will be born in {abs(age)} years.'
    return 'You were born this very year!'
