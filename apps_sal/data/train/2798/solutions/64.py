def to_alternating_case(string):

    list1 = []
    for letter in string:
        if letter.isupper():
            list1.append(letter.lower())
        else:
            list1.append(letter.upper())

    alt_string = ''.join(list1)
    return alt_string
