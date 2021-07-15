def people_with_age_drink(age):
    switcher={
        1: 'drink toddy',
        2: 'drink coke',
        3: 'drink beer',
        4: 'drink whisky'
    }
    if age < 14:  return switcher.get(1,None)
    elif 14 <= age < 18:  return switcher.get(2,None)
    elif 18 <= age < 21:  return switcher.get(3,None)
    elif 21 <= age:  return switcher.get(4,None)
