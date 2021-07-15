def people_with_age_drink(age):
    j = True
    if age < 14: 
        j = 'drink toddy'
    elif age < 18:
        j = 'drink coke'
    elif age < 21:
        j = 'drink beer'
    elif age >= 21:
        j = 'drink whisky'    
    return j
