def to_alternating_case(string):
    result = ''
    for i in string:
        for j in i:
            if j.islower():
                cap = j.upper()
                result = result + cap
            else:
                small = j.lower()
                result = result + small
    return result
