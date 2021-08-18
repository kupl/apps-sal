def get_age(age):
    for item in age:
        if item.isnumeric():
            return int(item)
