def first_non_repeating_letter(string):
    counter = 0
    for x in string:
        for y in string.lower():
            if y == x.lower():
                counter += 1
        if counter == 1:
            return x
        counter = 0
    return ''
