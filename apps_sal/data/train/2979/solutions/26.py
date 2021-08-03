def get_age(age):
    int_age = [str(i) for i in str(age)]
    return int(int_age[0])


print(get_age('2 years old'))
