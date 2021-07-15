def get_drink_by_profession(param):
    d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster Craft Beer", "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}
    if param.title() in d:
        return d[param.title()]
    else:
        return "Beer"
