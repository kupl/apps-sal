def people_with_age_drink(age):
    if age <= 13:
        return "drink toddy"
    elif age in range(14, 18):
        return "drink coke"
    elif age in range(18, 21):
        return "drink beer"
    elif age >= 21:
        return "drink whisky"

