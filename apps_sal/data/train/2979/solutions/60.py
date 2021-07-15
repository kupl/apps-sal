def get_age(age):
    k = str(age)
    for i in k:
        if i.isdigit() == True:
            return int(i)
