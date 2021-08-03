def people_with_age_drink(age):
    if age >= 21:
        return 'drink whisky'
    elif age in range(18, 21):
        return 'drink beer'
    elif age in range(14, 18):
        return 'drink coke'
    elif age in range(0, 14):
        return 'drink toddy'
