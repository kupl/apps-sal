def get_drink_by_profession(param):
    dict = {"Jabroni" : "Patron Tequila", 
            "School counselor" : "Anything with Alcohol",
            "Programmer" : "Hipster Craft Beer",
            "Bike gang member" : "Moonshine",
            "Politician" : "Your tax dollars",
            "Rapper" : "Cristal"} 
    param = param.capitalize()
    if param in dict:
        return dict[param]
    return "Beer"
