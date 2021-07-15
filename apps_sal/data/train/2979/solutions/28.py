def get_age(age):
    return int(''.join([i for i in age.split() if i.isdigit()]))
