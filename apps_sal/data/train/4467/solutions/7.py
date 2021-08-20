def remember(str_):
    (first_occured, reported) = ([], [])
    for letter in str_:
        if letter not in first_occured:
            first_occured.append(letter)
        elif letter not in reported:
            reported.append(letter)
    return reported
