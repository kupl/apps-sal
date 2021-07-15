def get_drink_by_profession(param):
    #This function receives an input parameter and produces the corresponding output

    #Step 1 - Produce a dictionary
    Drinks = {'jabroni':'Patron Tequila',
            'school counselor':'Anything with Alcohol',
            'programmer':'Hipster Craft Beer',
            'bike gang member':'Moonshine',
            'politician':'Your tax dollars',
            'rapper':'Cristal'}
    #Step 2 - Turn input to lower case

    profession = param.lower()

    #Step 3 - A for loop that cycles through the keys and has conditional statement

    for key in Drinks:
        if key == profession:
            return Drinks[key]
    
    return 'Beer'
