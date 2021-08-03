def get_drink_by_profession(param):
    drink_dic = {'Jabroni': 'Patron Tequila', 'School Counselor': 'Anything with Alcohol',
                 'Programmer': 'Hipster Craft Beer', 'Bike Gang Member': 'Moonshine',
                 'Politician': 'Your tax dollars', 'Rapper': 'Cristal'}
    return drink_dic[param.title()] if param.title() in drink_dic else 'Beer'
