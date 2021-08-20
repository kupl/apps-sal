def get_drink_by_profession(param):
    if param.lower() in ['jabroni']:
        return 'Patron Tequila'
    elif param.lower() in ['school counselor']:
        return 'Anything with Alcohol'
    elif param.lower() in ['programmer']:
        return 'Hipster Craft Beer'
    elif param.lower() in ['bike gang member']:
        return 'Moonshine'
    elif param.lower() in ['rapper']:
        return 'Cristal'
    elif param.lower() in ['politician']:
        return 'Your tax dollars'
    else:
        return 'Beer'
