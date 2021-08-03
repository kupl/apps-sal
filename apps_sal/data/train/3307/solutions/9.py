def fat_fingers(string):
    if string == "":
        return string

    if string is None:
        return None

    new_string = ""
    caps_lock = False

    for l in string:
        if l.isalpha():
            if l.lower() == 'a':
                caps_lock = not caps_lock

            elif caps_lock and l.lower() == l:
                new_string += l.upper()

            elif caps_lock and l.upper() == l:
                new_string += l.lower()

            else:
                new_string += l
        else:
            new_string += l

    return new_string
