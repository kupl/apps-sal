def get_age(age):
    import re
    return int(re.findall(r'\A\d', age)[0])
    # your code here
