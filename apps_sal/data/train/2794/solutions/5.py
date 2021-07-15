def calculate_age(year_of_birth, current_year):
    year = (year_of_birth - current_year)
    c1 = f"You are {abs(year)} {['year','years'][abs(year)!=1]} old."
    c2 = f"You will be born in {year} {['year','years'][year!=1]}."
    return 'You were born this very year!' if not year else [c1,c2][year >0 ]
