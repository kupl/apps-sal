def calculate_age(year_of_birth, current_year):
    if current_year - year_of_birth > 0: return 'You are %d year%s old.' %(current_year - year_of_birth, '' if current_year - year_of_birth == 1 else 's')
    elif current_year - year_of_birth < 0: return 'You will be born in %d year%s.' %(year_of_birth - current_year, '' if year_of_birth - current_year == 1 else 's')
    else: return 'You were born this very year!'
