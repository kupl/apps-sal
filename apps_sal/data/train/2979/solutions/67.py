def get_age(age):
    print('How old are you?')
    if type(age) == int:
        return age
    elif type(age) == str:
        ageInt = int(age[0])
        return ageInt
