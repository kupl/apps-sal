def people_with_age_drink(age):
    result = ""
    if(age < 14):
        result = "drink toddy"
    if(age >= 14 and age < 18):
        result = "drink coke"
    if(age >= 18 and age <= 21):
        result = "drink beer"
    if(age >= 21):
        result = "drink whisky"
    return result
