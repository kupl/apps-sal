def dating_range(age):
    if age < 15:
        return "%d-%d" % (.9*age, 1.1*age)
    else:
        return "%d-%d" % (age/2 + 7, (age - 7) * 2)
