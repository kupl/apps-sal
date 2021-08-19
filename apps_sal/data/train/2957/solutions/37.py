def get_drink_by_profession(param):
    jobName = param.upper()
    if jobName == 'JABRONI':
        return 'Patron Tequila'
    elif jobName == 'SCHOOL COUNSELOR':
        return 'Anything with Alcohol'
    elif jobName == 'PROGRAMMER':
        return 'Hipster Craft Beer'
    elif jobName == 'BIKE GANG MEMBER':
        return 'Moonshine'
    elif jobName == 'POLITICIAN':
        return 'Your tax dollars'
    elif jobName == 'RAPPER':
        return 'Cristal'
    else:
        return 'Beer'
