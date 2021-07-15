def get_age(age):
    girl_list = age.split()
    if int(girl_list[0]) > 0 and int(girl_list[0]) <= 9:
        return int(list(age)[0])
