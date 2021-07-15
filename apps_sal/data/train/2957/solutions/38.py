def get_drink_by_profession(param = 'anything else'):
    switcher = { 
        'Jabroni': 'Patron Tequila', 
        'School Counselor': 'Anything with Alcohol', 
        'Programmer': 'Hipster Craft Beer',
        'Bike Gang Member' : 'Moonshine',
        'Politician' : 'Your tax dollars',
        'Rapper' : 'Cristal',
    } 
    return switcher.get(param.lower().title(), 'Beer')
