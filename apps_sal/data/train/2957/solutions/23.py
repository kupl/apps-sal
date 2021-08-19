def get_drink_by_profession(param):
    shite = {'Jabroni': 'Patron Tequila', 'School Counselor': 'Anything with Alcohol', 'Programmer': 'Hipster Craft Beer', 'Bike Gang Member': 'Moonshine', 'Politician': 'Your tax dollars', 'Rapper': 'Cristal'}
    return shite.get(param.title(), 'Beer')
