def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif 13 < age < 18:
        return 'drink coke'
    elif 17 < age < 21:
        return 'drink beer'
    elif age > 20:
        return 'drink whisky'
