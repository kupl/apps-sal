def name_in_str(str, name):
    name = list(reversed(name.lower()))
    for c in str.lower():
        if c == name[-1]:
            name.pop()
        if not name:
            return True
    return False
