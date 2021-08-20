def reverse_number(number):
    splitted = [x for x in str(number)]
    if '-' in splitted:
        splitted.remove('-')
        splitted.reverse()
        splitted.insert(0, '-')
        return int(''.join(splitted))
    else:
        splitted.reverse()
        return int(''.join(splitted))
