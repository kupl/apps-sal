def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif 14 < age < 18:
        return 'drink coke'
    elif 18 < age < 21:
        return 'drink beer'
    elif age == 18:
        return 'drink beer'
    elif age == 14:
        return 'drink coke'
    elif age == 21:
        return 'drink whisky'
    elif age > 21:
        return 'drink whisky'
