def people_with_age_drink(age):
    res='drink {}'
    if age<14:
        return res.format('toddy')
    elif age<18:
        return res.format('coke')
    elif age<21:
        return res.format('beer')
    return res.format('whisky')

