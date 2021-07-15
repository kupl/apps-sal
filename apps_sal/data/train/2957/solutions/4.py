CLICHES = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer": "Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
}

def get_drink_by_profession(param):
    return CLICHES.get(param.lower(), "Beer")
