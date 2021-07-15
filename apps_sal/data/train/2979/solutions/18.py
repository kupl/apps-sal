def get_age(age):
    return [int(c) for c in age if c.isnumeric() == True][0]
