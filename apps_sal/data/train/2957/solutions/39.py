def get_drink_by_profession(param):
    dct = {"Jabroni": "Patron Tequila",
           "School Counselor": "Anything with Alcohol",
           "Programmer": "Hipster Craft Beer",
           "Bike Gang Member": "Moonshine",
           "Politician": "Your tax dollars",
           "Rapper": "Cristal"}
    return dct[param.title()] if param.title() in dct else 'Beer'
