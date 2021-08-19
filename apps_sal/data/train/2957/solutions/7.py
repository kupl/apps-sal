def get_drink_by_profession(param):
    param = param.title()
    menu = {'Jabroni': 'Patron Tequila', 'School Counselor': 'Anything with Alcohol', 'Programmer': 'Hipster Craft Beer', 'Bike Gang Member': 'Moonshine', 'Politician': 'Your tax dollars', 'Rapper': 'Cristal'}
    if param in menu.keys():
        return menu[param]
    else:
        return 'Beer'
