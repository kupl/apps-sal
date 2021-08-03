def people_with_age_drink(age):
    if age >= 21:
        return 'drink whisky'
    if age >= 18 and age < 21:
        return 'drink beer'
    if age >= 14 and age < 18:
        return 'drink coke'
    if age < 14:
        return 'drink toddy'
