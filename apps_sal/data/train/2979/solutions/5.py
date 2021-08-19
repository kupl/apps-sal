def get_age(age):
    age = age[0]
    age = int(age)
    if age > 9 or age < 0:
        return 0
    else:
        return age
