def capitalize(s, ind):
    new_string = ""
    for letter in range(len(s)):
        if letter in ind:
            new_string += s[letter].upper()
        else:
            new_string += s[letter]
    return new_string
