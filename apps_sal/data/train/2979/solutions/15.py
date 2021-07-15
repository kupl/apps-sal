def get_age(age):
    a = [int(s) for s in age.split() if s.isdigit()]
    for i in a:
        return i
