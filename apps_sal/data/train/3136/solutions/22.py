from bisect import bisect
def people_with_age_drink(age):
    r = {
        0: "drink toddy",
        1: "drink coke",
        2: "drink beer",
        3: "drink whisky"
    }
    return r[bisect([14, 18, 21], age)]
