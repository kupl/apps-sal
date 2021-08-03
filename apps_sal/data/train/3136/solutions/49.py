def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    if age < 18 and age > 13:
        return "drink coke"
    if age < 21 and age >= 18:
        return "drink beer"
    if age >= 21:
        return "drink whisky"
