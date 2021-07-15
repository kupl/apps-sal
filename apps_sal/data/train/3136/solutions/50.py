def people_with_age_drink(age):
    if age <= 13:
        return 'drink toddy'
    elif age <= 17 and age >= 14:
        return 'drink coke'
    elif age >= 21:
        return 'drink whisky'
    else:
        return 'drink beer'
