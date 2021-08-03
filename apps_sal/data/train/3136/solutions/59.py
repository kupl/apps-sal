def people_with_age_drink(age):
    drinks = {'Children': "drink toddy",
              'Teens': "drink coke",
              'Young': "drink beer",
              'Adults': "drink whisky"}
    if age < 14:
        return drinks['Children']
    if age < 18:
        return drinks['Teens']
    if age < 21:
        return drinks['Young']
    if age >= 21:
        return drinks['Adults']
