def get_age(age):
    return [int(s) for s in age.split() if s.isdigit()][0]
