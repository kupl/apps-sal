def people_with_age_drink(age):
    res = ""
    if age < 14:
        res = "drink toddy"
    elif age < 18:
        res = "drink coke"
    elif age < 21:
        res = "drink beer"
    else:
        res = "drink whisky"
    return res
