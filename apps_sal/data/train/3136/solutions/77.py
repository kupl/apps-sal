def people_with_age_drink(age):
    if age <= 13: 
        return "drink toddy"
    elif age <= 17:
        return "drink coke"
    elif age == 18 or age <= 20:
        return "drink beer"
    elif age > 20:
        return "drink whisky"
    

