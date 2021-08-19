def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age >= 21:
        return 'drink whisky'
    elif age < 18:
        return 'drink coke'
    elif age >= 18 < 21:
        return 'drink beer'
