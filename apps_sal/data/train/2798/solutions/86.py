def to_alternating_case(string):
    final = ""
    for i in string:
        if i == i.lower():
            final += i.upper()
        else:
            final += i.lower()
    return final
