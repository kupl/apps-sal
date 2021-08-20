def get_age(age):
    age = age.replace('years', '')
    age = age.replace('year', '')
    age = age.replace('old', '')
    age.rstrip()
    age = int(age)
    return age
