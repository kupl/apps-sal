def get_drink_by_profession(param):
    p = param.lower()
    bartender = {
        "jabroni": "Patron Tequila",
        "school counselor": "Anything with Alcohol",
        "programmer": "Hipster Craft Beer",
        "bike gang member": "Moonshine",
        "politician": "Your tax dollars",
        "rapper": "Cristal",
        "anything else": "Beer"

    }
    if p in bartender:
        return bartender[p]
    else:
        return "Beer"

    # code me!
