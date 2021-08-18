def get_drink_by_profession(param):

    Drinks = {'jabroni': 'Patron Tequila',
              'school counselor': 'Anything with Alcohol',
              'programmer': 'Hipster Craft Beer',
              'bike gang member': 'Moonshine',
              'politician': 'Your tax dollars',
              'rapper': 'Cristal'}

    profession = param.lower()

    for key in Drinks:
        if key == profession:
            return Drinks[key]

    return 'Beer'
