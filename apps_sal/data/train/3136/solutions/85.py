#this function tells you what you should drink based on your age.
def people_with_age_drink(age):
    drink="drink "
    if age<14:
        drink+="toddy"
    elif age<18:
        drink+="coke"
    elif age<21:
        drink+="beer"
    elif age>=21:
        drink+="whisky"
    return drink
