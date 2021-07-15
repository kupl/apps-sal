def people_with_age_drink(age):
    if age >=21:
        return "drink whisky"
    else:
        if age < 21 and age >=18:
            return "drink beer"
        else:
            if age < 18 and age >= 14:
                return "drink coke"
            else:
                return "drink toddy"

