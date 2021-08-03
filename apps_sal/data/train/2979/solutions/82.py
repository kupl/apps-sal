def get_age(age):
    str = ""
    for i in age:
        if i.isnumeric():
            str = str + i
    return int(str)
