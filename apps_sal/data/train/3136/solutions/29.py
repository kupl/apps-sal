def people_with_age_drink(age):
    a = [(14, 'drink toddy'), (18, 'drink coke'), (21, 'drink beer')]
    for i, d in a:
        if age < i:
            return d
    return 'drink whisky'
