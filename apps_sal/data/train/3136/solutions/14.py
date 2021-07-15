drinks = [
    ("whisky", 21),
    ("beer", 18),
    ("coke", 14),
]
def people_with_age_drink(age):
    return "drink " + next((drink for drink, age_limit in drinks if age >= age_limit), "toddy")
