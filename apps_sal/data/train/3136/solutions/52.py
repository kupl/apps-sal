def people_with_age_drink(age):
    (a, b, c) = (14, 18, 21)
    if age < a:
        return 'drink toddy'
    if a <= age < b:
        return 'drink coke'
    if b <= age < c:
        return 'drink beer'
    if age >= c:
        return 'drink whisky'
