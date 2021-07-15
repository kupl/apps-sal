def people_with_age_drink(age):
    if age in range(0,14):
        return 'drink toddy'
    elif age in range(13,18):
        return 'drink coke'
    elif age in range(18,21):
        return 'drink beer'
    else:
        return 'drink whisky'
