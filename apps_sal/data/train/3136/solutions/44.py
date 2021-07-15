def people_with_age_drink(age):
    if not(age) > 13:
        return 'drink toddy'
    elif age > 13 and not (age) >= 18:
        return 'drink coke'
    elif age >= 18 and not (age) > 20:
        return 'drink beer'
    else:
        return 'drink whisky'
