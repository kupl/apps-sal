def people_with_age_drink(age):
    for a in [[21, 'whisky'], [18, 'beer'], [14, 'coke'], [0, 'toddy']]:
        if age >= a[0]:
            return 'drink {0}'.format(a[1])
