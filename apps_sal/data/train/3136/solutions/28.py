def people_with_age_drink(age):
    for (limit, drink) in [(14, 'toddy'), (18, 'coke'), (21, 'beer')]:
        if age < limit:
            return 'drink ' + drink
    return 'drink whisky'
