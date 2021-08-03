def get_drink_by_profession(param):
    drink_list = {'Jabroni': 'Patron Tequila',
                  'School Counselor': "Anything with Alcohol",
                  'Programmer': 'Hipster Craft Beer',
                  'Bike Gang Member': 'Moonshine',
                  'Politician': 'Your tax dollars',
                  'Rapper': 'Cristal', }
    param = param.title()
    try:
        return (drink_list)[param]
    except:
        return 'Beer'
