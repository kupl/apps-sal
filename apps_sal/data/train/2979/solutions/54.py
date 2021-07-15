def get_age(age):
    res = int(age.split()[0])
    return 0 if 0 > res > 9 else res
