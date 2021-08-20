def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif 14 <= age <= 17:
        return 'drink coke'
    elif 17 < age < 21:
        return 'drink beer'
    else:
        return 'drink whisky'
