def get_drink_by_profession(x):
    return {'jabroni': 'Patron Tequila', 'school counselor': 'Anything with Alcohol', 'programmer': 'Hipster Craft Beer', 'bike gang member': 'Moonshine', 'politician': 'Your tax dollars', 'rapper': 'Cristal'}.get(x.lower()) or 'Beer'
