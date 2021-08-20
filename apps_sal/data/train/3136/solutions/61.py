def people_with_age_drink(age):
    if age <= 13:
        return 'drink toddy'
    elif 13 < age <= 17:
        return 'drink coke'
    elif 17 < age <= 20:
        return 'drink beer'
    else:
        return 'drink whisky'
