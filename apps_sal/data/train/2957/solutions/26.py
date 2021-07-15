def get_drink_by_profession(param):
    d = {"jabroni": "Patron Tequila", "school counselor" : "Anything with Alcohol", "programmer" : "Hipster Craft Beer", "bike gang member" : "Moonshine", "politician":"Your tax dollars", "rapper":"Cristal", "anything else":"Beer"}
    return d[param.lower()] if param.lower() in d else "Beer"
