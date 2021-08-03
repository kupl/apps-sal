def to_underscore(string):
    string = str(string)
    new = []
    for s in string:
        if not new:
            new.append(s)
        else:
            if s.isupper():
                new.append("_")
            new.append(s)
    return "".join(new).lower()
