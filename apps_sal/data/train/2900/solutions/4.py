def string_transformer(s):
    s = s.split(" ")
    s = s[::-1]
    s = " ".join(s)
    result = ""

    for letter in s:
        if letter.islower():
            result = result + letter.upper()
        elif letter.isupper():
            result = result + letter.lower()
        else:
            result = result + letter

    return result
