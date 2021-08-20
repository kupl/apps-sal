def people_with_age_drink(age: int) -> str:
    """ Get what people should drink based on their age. """
    return f"drink {('toddy' if age < 14 else 'coke' if age < 18 else 'beer' if age < 21 else 'whisky')}"
