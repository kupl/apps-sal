def to_underscore(string):
    string = str(string)
    camel_case = string[0].lower()
    for c in string[1:]:
        camel_case += '_{}'.format(c.lower()) if c.isupper() else c
    return camel_case
