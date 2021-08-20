def alternateCase(s):
    new = ''
    for let in s:
        if let.isupper():
            new += let.lower()
        elif let.islower():
            new += let.upper()
        else:
            new += let
    return new
