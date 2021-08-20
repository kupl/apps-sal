def get_drink_by_profession(param):
    param = param.lower()
    profs = {'jabroni': 'Patron Tequila', 'school counselor': 'Anything with Alcohol', 'programmer': 'Hipster Craft Beer', 'bike gang member': 'Moonshine', 'politician': 'Your tax dollars', 'rapper': 'Cristal'}
    if param in profs:
        return profs[param]
    else:
        return 'Beer'
