def to_alternating_case(string):
    word = ''
    for el in string:
        if el ==el.upper():
            word+=el.lower()
        elif el ==el.lower():
            word+=el.upper()
        else:
            word += el.upper()
    return word
