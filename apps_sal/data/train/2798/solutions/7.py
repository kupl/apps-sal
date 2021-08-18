def to_alternating_case(string):
    s = ''
    for i in string:
        i.split()
        if i.islower():
            s = s + i.upper()
        if i.isupper():
            s = s + i.lower()
        if i.isspace():
            s = s + ' '
        if i.isdigit():
            s = s + str(i)
        if i == '.':
            s = s + str('.')
        if i == '<':
            s = s + str('<')
        if i == '=':
            s = s + str('=')
        if i == '>':
            s = s + str('>')
        if i == "'":
            s = s + str("'")
        if i == '?':
            s = s + str('?')
        if i == ';':
            s = s + str(';')
        if i == ',':
            s = s + str(',')
        if i == "/":
            s = s + str("/")
        if i == '\'':
            s = s + str('\'')
        if i == "|":
            s = s + str("|")
        if i == "!":
            s = s + str("!")
        if i == ":":
            s = s + str(":")

    return s
