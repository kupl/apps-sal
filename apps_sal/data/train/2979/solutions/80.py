def get_age(age):
    res = [int(i) for i in age.split() if i.isdigit()]
    return res[0]
