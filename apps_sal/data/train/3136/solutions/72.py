def people_with_age_drink(age):
    drinks = {'14': 'drink toddy', '18': 'drink coke', '21': 'drink beer', '100': 'drink whisky'}
    for key in drinks:
        if age < int(key):
            return drinks[key]
