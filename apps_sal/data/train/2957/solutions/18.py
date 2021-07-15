def get_drink_by_profession(param):
    param=param.lower()
    if "jabroni" in param:
        return "Patron Tequila"
    if param== "school counselor":
        return "Anything with Alcohol"
    if param== "programmer":
        return "Hipster Craft Beer"
    if param=="bike gang member":
        return "Moonshine" 
    if param=="politician":
       return "Your tax dollars" 
    if param=="rapper":
       return "Cristal" 
    return "Beer"
