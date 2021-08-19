def get_drink_by_profession(param):
    # code me!
    drinkList = {"jabroni": "Patron Tequila", "school counselor": "Anything with Alcohol", "programmer": "Hipster Craft Beer", "bike gang member": "Moonshine", "politician": "Your tax dollars", "rapper": "Cristal"
                 }
    return drinkList[param.lower()] if param.lower() in list(drinkList.keys()) else "Beer"
