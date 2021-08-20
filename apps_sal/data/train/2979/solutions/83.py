def get_age(age):
    str = age
    str_list = str.split()
    for element in str_list:
        if element.isdigit():
            return int(element)
