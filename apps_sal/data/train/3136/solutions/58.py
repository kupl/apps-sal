def people_with_age_drink(age):
    drink = {
        14: 'toddy',
        18: 'coke',
        21: 'beer'
    }
    for d in drink:
        if age < d:
            return 'drink ' + drink[d]
    return 'drink whisky'
