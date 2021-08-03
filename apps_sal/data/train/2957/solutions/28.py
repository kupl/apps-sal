thisdict = {
    "Jabroni": "Patron Tequila",
    "School Counselor": "Anything with Alcohol",
    "Programmer": "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine",
    "Politician": "Your tax dollars",
    "Rapper": "Cristal"
}


def get_drink_by_profession(param):
    formatted = param.title()
    drink = "Beer"
    if formatted in thisdict:
        drink = thisdict.get(formatted)
    return(drink)
