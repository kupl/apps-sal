def get_age(age):
    import re
    return int(re.findall('\\A\\d', age)[0])
