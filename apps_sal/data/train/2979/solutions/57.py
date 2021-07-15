def get_age(age):
    if "year old" in age:
        return 1
    else:
        return int(age[0])
