def name_in_str(text, name):
    for c in text.lower():
        if c == name[0].lower():
            name = name[1:]
            if not name:
                return True
    return False
