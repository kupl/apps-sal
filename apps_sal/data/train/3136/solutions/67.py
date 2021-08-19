def people_with_age_drink(age):
    drink = ''
    if 0 <= age < 14:
        drink = 'drink toddy'
    if 14 <= age < 18:
        drink = 'drink coke'
    if 18 <= age < 21:
        drink = 'drink beer'
    if 21 <= age:
        drink = 'drink whisky'
    return drink


age = people_with_age_drink(0)
print(age)
