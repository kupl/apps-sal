def people_with_age_drink(age):
    return 'drink toddy'*(age<14) or 'drink coke'*(age<18) or 'drink beer'*(age<21) or 'drink whisky'
