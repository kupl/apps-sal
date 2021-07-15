def dating_range(age):
    min = age/2 + 7 if age > 14 else age-0.1*age
    max = (age-7)*2 if age > 14 else age+0.1*age
    return "{}-{}".format(int(min), int(max))
