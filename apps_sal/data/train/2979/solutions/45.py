def get_age(age):
    age = list(age.split(" "))[0]
    if age.isdigit():
        return int(age)
    return 0
