def to_alternating_case(string):

    fs =""
    for x in string:
        if x.isupper():
            fs += x.lower()
        else:
            fs += x.upper()
    return fs
