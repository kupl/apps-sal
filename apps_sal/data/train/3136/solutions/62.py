def people_with_age_drink(a):
    print(a)
    foo = ["drink toddy", "drink coke", "drink beer", "drink whisky"]
    if a >= 18:
        if a < 21:
            return foo[2]
        return foo[3]
    elif a < 18:
        if a < 14:
            return foo[0]
        return foo[1]

