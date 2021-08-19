def people_with_age_drink(age):
    for (lim, drink) in [(14, 'toddy'), (18, 'coke'), (21, 'beer'), (float('inf'), 'whisky')]:
        if age < lim:
            return 'drink ' + drink
