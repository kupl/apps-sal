def people_with_age_drink(age):
    print(age)
    if (age >= 0 and age <= 13):
        return 'drink toddy'
    elif (age >= 14 and age <= 17):
        return 'drink coke'
    elif (age >= 18 and age <= 20):
        return 'drink beer'
    else:
        return 'drink whisky'
