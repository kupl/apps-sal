def get_drink_by_profession(param):
    drink_dict = {
        "Jabroni": "Patron Tequila",
        "School Counselor": "Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal",
        "anything else": "Beer"
    }
    param = param.title()
    if param in drink_dict.keys():
        return drink_dict[param]
    else:
        return "Beer"
