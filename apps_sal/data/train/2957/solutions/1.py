def get_drink_by_profession(param):
    return {'Jabroni': 'Patron Tequila', 'School Counselor': 'Anything with Alcohol', 'Programmer': 'Hipster Craft Beer', 'Bike Gang Member': 'Moonshine', 'Politician': 'Your tax dollars', 'Rapper': 'Cristal'}.get(param.title(), 'Beer')
