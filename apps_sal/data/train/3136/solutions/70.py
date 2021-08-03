def people_with_age_drink(age):

    s = ''

    if age > 20:
        s = 'whisky'
    if age < 21:
        s = 'beer'
    if age < 18:
        s = 'coke'
    if age < 14:
        s = 'toddy'

    return 'drink ' + s
