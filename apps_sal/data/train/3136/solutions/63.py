def people_with_age_drink(age: int) -> str:
    """ Get what people should drink based on their age. """
    drink_rule = {
        age < 14: "toddy",
        14 <= age < 18: "coke",
        18 <= age < 21: "beer",
        age >= 21: "whisky"
    }
    return f"drink {drink_rule[True]}"
