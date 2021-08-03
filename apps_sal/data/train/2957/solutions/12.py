def get_drink_by_profession(param):
    param = param.lower().title()
    L = ["Jabroni", "School Counselor", "Programmer", "Bike Gang Member", "Politician", "Rapper"]
    L1 = ["Patron Tequila", "Anything with Alcohol", "Hipster Craft Beer", "Moonshine", "Your tax dollars", "Cristal"]
    if param in L:
        n = L.index(param)
        return L1[n]
    else:
        return "Beer"
